import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")
        self.root.geometry("400x200")

        # Initialize variables
        self.image_path = None
        self.watermark_text = tk.StringVar()

        # Load Image Button
        self.load_image_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_image_button.pack(pady=10)

        # Watermark Entry
        self.label = tk.Label(root, text="Enter Watermark Text:")
        self.label.pack()
        self.watermark_entry = tk.Entry(root, textvariable=self.watermark_text)
        self.watermark_entry.pack()

        # Apply Watermark Button
        self.apply_watermark_button = tk.Button(root, text="Apply Watermark", command=self.apply_watermark)
        self.apply_watermark_button.pack(pady=10)

        # Save Image Button
        self.save_image_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_image_button.pack(pady=10)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            tk.messagebox.showinfo("Image Loaded", "Image loaded successfully!")

    def apply_watermark(self):
        if not self.image_path:
            tk.messagebox.showwarning("Warning", "Please load an image first.")
            return

        # Load the image
        with Image.open(self.image_path) as img:
            draw = ImageDraw.Draw(img)

            # Define font and size (adjust as needed)
            font = ImageFont.truetype("arial.ttf", 36)
            text = self.watermark_text.get()

            # Set position for watermark (bottom-right corner)
            text_width, text_height = draw.textsize(text, font=font)
            x, y = img.width - text_width - 10, img.height - text_height - 10

            # Apply watermark text
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))  # White text with opacity

            # Save modified image temporarily
            img.save("temp_watermarked_image.png")
            tk.messagebox.showinfo("Watermark Applied", "Watermark added successfully!")

    def save_image(self):
        if not self.image_path:
            tk.messagebox.showwarning("Warning", "Please load an image first.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            with Image.open("temp_watermarked_image.png") as img:
                img.save(save_path)
            tk.messagebox.showinfo("Image Saved", "Image saved successfully!")

# Initialize Tkinter root and app
root = tk.Tk()
app = WatermarkApp(root)
root.mainloop()
