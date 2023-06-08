import tkinter as tk
import utility as util
import cv2
from PIL import Image, ImageTk
import numpy as np
import os
import subprocess
import datetime


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1000x500+100+100")
        self.login_main_window = util.get_button(
            self.main_window, "Login", "green", self.login
        )
        self.login_main_window.place(x=750, y=300)
        self.register_main_window = util.get_button(
            self.main_window, "register", "gray", self.register, fg="black"
        )
        self.register_main_window.place(x=750, y=400)
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)
        self.db_dir = "./db"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log = "./log.txt"

    def add_webcam(self, label):
        if "cap" not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        frame = np.flip(frame, axis=1)  # Flip horizontally
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_PIL = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_PIL)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        self._label.after(20, self.process_webcam)

    def register(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1000x500+300+150")
        self.accept_register_window = util.get_button(
            self.register_new_user_window,
            "accept",
            "green",
            self.accept_register_newuser,
        )
        self.accept_register_window.place(x=750, y=300)

        self.tryagain_register_window = util.get_button(
            self.register_new_user_window,
            "try again",
            "red",
            self.tryagain_register_newuser,
        )
        self.tryagain_register_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entrytext_new_user = util.get_entry_text(self.register_new_user_window)
        self.entrytext_new_user.place(x=750, y=150)

        self.text_label_register_new = util.get_text_label(
            self.register_new_user_window, "please\nenter your name :"
        )
        self.text_label_register_new.place(x=750, y=70)

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_PIL)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def tryagain_register_newuser(self):
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()

    def login(self):
        unknown_img_path = "./.tmp.jpg"
        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)
        output = str(
            subprocess.check_output(["face_recognition", self.db_dir, unknown_img_path])
        )
        os.remove(unknown_img_path)
        # print(output)
        name = output.split(",")[1][:-5]
        print(name)
        if name in ["unkown_person", "no_persons_found"]:
            util.msg_box("Unkown user", "please register and try again")
        else:
            util.msg_box("welcome", "welcome {}".format(name))
            with open(self.log, "a") as f:
                f.write("name :{} , Time: {}\t".format(name, datetime.datetime.now()))
                f.close()

    def accept_register_newuser(self):
        name = self.entrytext_new_user.get(1.0, "end-1c")
        cv2.imwrite(
            os.path.join(self.db_dir, "{}.jpg".format(name)),
            self.register_new_user_capture,
        )
        util.msg_box("Done", "user was created successfully")
        self.register_new_user_window.destroy()


if __name__ == "__main__":
    app = App()
    app.start()
