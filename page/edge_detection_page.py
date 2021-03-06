import tkinter as tk
import settings


class EdgeDetectionPage(tk.Frame):
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl

        label = tk.Label(
            self,
            text="Kantenerkennung Methode und Vorschau"
        )
        label.grid(row=0, column=0)

        self.output_widget = tk.Label(self)
        self.output_widget.grid(row=1, column=0)

        self.method_var = tk.StringVar(self)
        self.method_var.set("bw_threshold_linear")

        # OptionMenu needs to have its command when created
        self.method_selection = tk.OptionMenu(
            self,
            self.method_var,
            "sobel_canny",
            "bw_threshold_linear",
            command=self.ctrl.update_detection_method
        )
        self.method_selection.grid(row=2, column=0)

        self.scale_frame = tk.Frame(self)
        self.scale_frame.grid(row=3, column=0)

        self.top_scale = tk.Scale(
            self.scale_frame,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            sliderlength=20,
            length=150,
            label="Threshold"
        )
        self.top_scale.set(settings.BW_DEFAULT_THRESHOLD)
        self.top_scale.grid(row=0, column=0)

        self.bottom_scale = tk.Scale(
            self.scale_frame,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            sliderlength=20,
            length=150
        )
        self.bottom_scale.set(settings.SOBEL_DEFAULT_BOTTOM)
        self.bottom_scale.grid(row=0, column=1)
        self.bottom_scale.grid_remove()

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=4, column=0)

        self.test_button = tk.Button(
            self.button_frame,
            text="Kanten erkennen"
        )
        self.test_button.grid(row=0, column=0)

        self.send_data_button = tk.Button(
            self.button_frame,
            text="Weiter"
        )
        self.send_data_button.grid(row=0, column=1, padx=(100, 5))

        self.ctrl.connect_page(self)
    # end __init__

    def before_hide(self):
        self.ctrl.before_hide()
    # end before_hide

    def before_show(self):
        self.ctrl.before_show()
    # end before_show

    def update_data(self):
        self.ctrl.update_data()
