from tkinter import *
from tkinter import messagebox
from app_brain import AppBrain

class Window:
    """Class of a window interface."""

    def __init__(self) -> None:
        """Init window interface."""
        self.window = Tk()
        self.window.title("Eating Calculator")
        self.window.minsize(width = 462, height = 424)
        self.window.config(padx=0, pady=0, bg="lightblue")
        self.bg = PhotoImage(file = "./img/vege.png")
        self.label_bg = Label(self.window, image = self.bg, highlightthickness=0)
        self.label_bg.grid(row=0, column=0, rowspan=9, columnspan=2)
        """Buttons"""
        self._add_meal = Button(text="add meal", width = 25, bg="#03bafc", command=self.button_add_meal)
        self._add_meal.grid(row=0, column=0)
        self._set_daily_goal = Button(text="set daily goal", width = 25, bg="white", command=self.button_set_daily_goal)
        self._set_daily_goal.grid(row=0, column=1)
        self._calculate_by_product = Button(text="calculate by product", width = 25, bg="grey", command=self.button_else_to_eat)
        self._calculate_by_product.grid(row=1, column=0)
        self._calculate_by_meal = Button(text="calculate by meal", width = 25, bg="grey", command=self.button_adjust_last_meal_solver)
        self._calculate_by_meal.grid(row=1, column=1)
        self._energy_content_eaten_today = Button(text="energy content eaten today", width = 25, command=self.button_already_eaten_today)
        self._energy_content_eaten_today.grid(row=2, column=0)
        self._products_eaten_today = Button(text="products eaten today", width = 25, command=self.button_print_daily_eaten_products)
        self._products_eaten_today.grid(row=2, column=1)

        self.window.mainloop()

    def button_add_meal(self) -> None:
        """Add meal button execute."""
        def submit() -> None:
            """Submit button execute inside."""
            query = entry1.get()
            label1.destroy()
            entry1.destroy()
            submit_button.destroy()
            messagebox.showinfo(title="information", message=f"{AppBrain().add_meal(query)}")
        label1 = Label(text="What have you eaten?", bg="silver", highlightthickness=2, highlightbackground="grey")
        label1.grid(row=3, column=0, columnspan=2, pady=0)
        entry1 = Entry(width=50, state="normal")
        entry1.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        submit_button = Button(text="submit", width=5, bg="#03bafc", command=submit)
        submit_button.grid(row=4, column=1, sticky="e", padx=20)

    def button_set_daily_goal(self) -> None:
        """Set daily goal button execute."""
        def submit() -> None:
            """Sumit button execute inside."""
            proteins = entry1.get()
            carbohydrates = entry2.get()
            fats = entry3.get()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            submit_button.destroy()
            messagebox.showinfo(title="information", message=f"{AppBrain().set_calories_goal(proteins, carbohydrates, fats)}")
        label1 = Label(text="Type your proteins goal", bg="silver", highlightthickness=2, highlightbackground="grey")
        label1.grid(row=3, column=0, columnspan=2, pady=0)

        label2 = Label(text="Type your carbohydrates goal", bg="silver", highlightthickness=2, highlightbackground="grey")
        label2.grid(row=5, column=0, columnspan=2, pady=0)

        label3 = Label(text="Type your fats goal", bg="silver", highlightthickness=2, highlightbackground="grey")
        label3.grid(row=7, column=0, columnspan=2, pady=0)

        entry1 = Entry(width=10, state="normal")
        entry1.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        entry2 = Entry(width=10, state="normal")
        entry2.grid(row=6, column=0, columnspan=2, padx=0, pady=0)

        entry3 = Entry(width=10, state="normal")
        entry3.grid(row=8, column=0, columnspan=2, padx=0, pady=0)

        submit_button = Button(text="submit", width=5, bg="#03bafc", command=submit)
        submit_button.grid(row=8, column=1, sticky="e", padx=20)

    def button_else_to_eat(self) -> None:
        """Else to eat button execute."""
        def submit() -> None:
            """Sumit button execute inside."""
            query = entry1.get()
            label1.destroy()
            entry1.destroy()
            submit_button.destroy()
            messagebox.showinfo(title="information", message=f"{AppBrain().else_to_eat(query)}")
        label1 = Label(text="Type your products", bg="silver", highlightthickness=2, highlightbackground="grey")
        label1.grid(row=3, column=0, columnspan=2, pady=0)
        
        entry1 = Entry(width=50, state="normal")
        entry1.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        submit_button = Button(text="submit", width=5, bg="#03bafc", command=submit)
        submit_button.grid(row=4, column=1, sticky="e", padx=20)

    def button_adjust_last_meal_solver(self) -> None:
        """Adjust last meal solver button execute."""
        def submit() -> None:
            """Sumit button execute inside."""
            query = entry1.get()
            label1.destroy()
            entry1.destroy()
            submit_button.destroy()
            messagebox.showinfo(title="information", message=f"{AppBrain().adjust_last_meal_solver(query)}")
        label1 = Label(text="Type your products", bg="silver", highlightthickness=2, highlightbackground="grey")
        label1.grid(row=3, column=0, columnspan=2, pady=0)

        entry1 = Entry(width=50, state="normal")
        entry1.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        submit_button = Button(text="submit", width=5, bg="#03bafc", command=submit)
        submit_button.grid(row=4, column=1, sticky="e", padx=20)

    def button_already_eaten_today(self) -> None:
        """Already eaten button execute."""
        messagebox.showinfo(title="information", message=f"{AppBrain().already_eaten_today()}")

    def button_print_daily_eaten_products(self) -> None:
        """Daily eaten products button execute."""
        messagebox.showinfo(title="information", message=f"{AppBrain().print_daily_eaten_products()}")