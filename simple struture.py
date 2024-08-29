import tkinter as tk
from tkinter import ttk

class Portfolio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Portfolio")
        self.geometry("800x600")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        self.home_frame = tk.Frame(self.notebook)
        self.about_frame = tk.Frame(self.notebook)
        self.projects_frame = tk.Frame(self.notebook)
        self.contact_frame = tk.Frame(self.notebook)

        self.notebook.add(self.home_frame, text="Home")
        self.notebook.add(self.about_frame, text="About")
        self.notebook.add(self.projects_frame, text="Projects")
        self.notebook.add(self.contact_frame, text="Contact")

        self.home_content()
        self.about_content()
        self.projects_content()
        self.contact_content()

    def home_content(self):
        tk.Label(self.home_frame, text="Welcome to my portfolio!", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.home_frame, text="I'm a software developer with a passion for creating innovative solutions.").pack()
        tk.Label(self.home_frame, text="Take a look around to learn more about me and my work.").pack()

    def about_content(self):
        tk.Label(self.about_frame, text="About Me", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.about_frame, text="I have a degree in Computer Science and have been working in the industry for 5 years.").pack()
        tk.Label(self.about_frame, text="I'm proficient in a range of programming languages, including Python, Java, and JavaScript.").pack()

    def projects_content(self):
        tk.Label(self.projects_frame, text="My Projects", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.projects_frame, text="Project 1: A web scraper built with Python and BeautifulSoup.").pack()
        tk.Label(self.projects_frame, text="Project 2: A mobile app built with Java and Android Studio.").pack()

    def contact_content(self):
        tk.Label(self.contact_frame, text="Get in Touch", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.contact_frame, text="Email: [example@example.com](mailto:example@example.com)").pack()
        tk.Label(self.contact_frame, text="Phone: 555-555-5555").pack()

if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.mainloop()
