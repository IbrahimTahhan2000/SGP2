from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from ultralytics import YOLO
import os
from django.conf import settings
from django.http import JsonResponse

# Construct the path to ASL.pt dynamically
model_path = os.path.join(settings.BASE_DIR, 'recognition/static/recognition/models/ASL.pt')

# Load the YOLO model
model = YOLO(model_path)

# Define sequences and phrases in order
sequences = [
    {
        'sequence': ['gaaf','laam','aleff','ain','waw','dal','bb',
                     'ra','bb',
                     'aleff','laam','nun','aleff','seen'],
        'phrase': 'قل أعوذ برب الناس',
        'order': 0,
        'index': 0,
        'completed': False
    },
    {
        'sequence': ['meem','laam','kaaf','aleff','laam','nun','aleff','seen'],
        'phrase': 'ملك الناس',
        'order': 1,
        'index': 0,
        'completed': False
    },
    {
        'sequence': ['aleff','laam','ha','aleff','laam','nun','aleff','seen'],
        'phrase': 'اله الناسِ',
        'order': 2,
        'index': 0,
        'completed': False
    },
    {
        'sequence': ['meem','nun','sheen','ra',
                     'aleff','laam','waw','seen','waw','aleff','seen'
            ,'aleff','laam','khaa','nun','aleff','seen'],
        'phrase': 'من شر الوسواس الخناس',
        'order': 3,
        'index': 0,
        'completed': False
    },
    {
        'sequence': ['aleff','laam','thal','yaa',
                     'yaa','waw','seen','waw','seen',
                     'fa','yaa','saad','dal','waw','ra'
                     'aleff','laam','nun','aleff','seen'],
        'phrase': 'الذي يوسوس في صدور الناس',
        'order': 4,
        'index': 0,
        'completed': False
    },
    {
        'sequence': ['meem','nun','aleff','laam','jeem','nun','taa',
                     'waw','aleff','laam','nun','aleff','seen'],
        'phrase': 'من الجنّة والناسَ',
        'order': 5,
        'index': 0,
        'completed': False
    },
]

# Track current sequence order
current_order = 0

# Webcam feed generator
def webcam_feed_al_nas():
    global current_order

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Perform detection and tracking
        results = model.track(frame, persist=True)
        annotated_frame = results[0].plot()

        # Check detections for the current sequence
        if results[0].boxes.data.tolist():
            detection = results[0].boxes.data.tolist()[0]  # Get the first detected object
            confidence = detection[-2]  # Confidence of the detection
            class_id = int(detection[-1])  # Class ID of the detection
            label = model.names[class_id]  # Get the class label

            # Process only the current sequence based on the order
            current_sequence = next((seq for seq in sequences if seq['order'] == current_order), None)
            if current_sequence and not current_sequence['completed']:
                # Match label to the current step in the sequence
                if label == current_sequence['sequence'][current_sequence['index']] and confidence > 0.80:
                    current_sequence['index'] += 1  # Move to the next character in the sequence

                    # If the sequence is completed
                    if current_sequence['index'] == len(current_sequence['sequence']):
                        current_sequence['completed'] = True
                        print(f"Sequence completed: {current_sequence['phrase']}")
                        current_order += 1  # Move to the next sequence in order

        # Encode the frame for streaming
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

# View to stream the webcam feed
def video_feed_al_nas(request):
    """Stream video feed to the browser."""
    return StreamingHttpResponse(webcam_feed_al_nas(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# API endpoint to check sequence statuses
def check_sequence_status_al_nas(request):
    # Check the phrases for completed sequences in order
    completed_phrases = [seq['phrase'] for seq in sequences if seq['completed']]
    return JsonResponse({'completed_phrases': completed_phrases})

def reset_sequences_al_nas(request):
    global current_order
    current_order = 0  # Reset the current order

    # Reset all sequences for the current Surah
    for seq in sequences:
        seq['index'] = 0
        seq['completed'] = False

    return JsonResponse({'message': 'Sequences reset successfully'})

def get_current_sequence_status_al_nas(request):
    # Find the current sequence
    current_sequence = next((seq for seq in sequences if seq['order'] == current_order), None)
    if current_sequence:
        return JsonResponse({
            'phrase': current_sequence['phrase'],
            'sequence': current_sequence['sequence'],
            'current_index': current_sequence['index'],
            'completed': current_sequence['completed']
        })
    else:
        return JsonResponse({'phrase': '', 'sequence': [], 'current_index': 0, 'completed': True})

# View to render the page
def surat_al_fatiha(request):
    return render(request, 'recognition/surat_al_nas.html')
