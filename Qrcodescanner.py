import tkinter
import cv2
from pyzbar.pyzbar import decode
import webbrowser
import subprocess
import re

def scan_qr_code():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray)

        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            print("Scanned Data:", data)

            
            if data.startswith('http://') or data.startswith('https://'):
                webbrowser.open(data)  
            else:
                
                subprocess.run(['echo', data], shell=True)

            
            cv2.putText(frame, data, (40, 40), cv2.FONT_ITALIC, 2, (0, 255, 0), 3)
        
        cv2.imshow("QR Code Scanner app ", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()

def open_url(url):
    webbrowser.open(url)


def handle_scanned_content(data):
    root = tkinter.Tk()
    root.title("QR Code Scanner app ")
    label = tkinter.Tk.Label(root, text="Scanned Data:")
    label.pack()
    result_label = tkinter.Tk.Label(root, text=data)
    result_label.pack()

    frame = tkinter.Tk.Frame(root, padx=10, pady=10)
    frame.pack()

    label = tkinter.Tk.Label(frame, text="Scanned Data:")
    label.pack()

    result_label = tkinter.Tk.Label(frame, text=data, wraplength=300)
    result_label.pack()

   
    if re.match(r'https?://\S+', data):
        open_button = tkinter.Tk.Button(root, text="Open URL", command=lambda url=data: open_url(url))
        open_button.pack()
    
    elif re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data):
        print("Scanned Email:", data)
    
    else:
        print("Scanned Text:", data)
        
    root.mainloop()

def scan():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2BGRAY)
        decoded = decode(gray)

        for obj in decoded:
            data = obj.data.decode('utf-8')
            print("Scanned Data:", data)

            
            handle_scanned_content(data)

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

scan()