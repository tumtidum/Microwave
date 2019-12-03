"""Microwave Converter - v0.0.1 - Python 3.7 - tumtidum.

Calculate the recommended preparation time of a TV dinner for
a microwave with a different power configuration (Watt).
The calculation is based on the total amount of energy (Joule).

"""

from tkinter import ttk, Tk, Frame, StringVar, BitmapImage, N, W, E, S


class App(Frame):
    """Main application (tkinter GUI)."""

    def __init__(self, root):
        """Summary here."""
        Frame.__init__(self, root)

        def only_numbers(char):
            """Restricts the user input to numbers only."""
            return char.isdigit()

        def calculator(*args):
            """Calculate all values.

            Parameters
            ----------
            *args : integers
                Recommended power of the microwave for preparation.
                Recommended time for the preparation.
                Power of the user's own microwave.

            Returns
            -------
            type : integers
                Recommended time for the preparation of the TV dinner
                using the user's own microwave.

            """
            try:
                recommended_pwr = int(watt.get())
                recommended_min = float(minutes.get())
                recommended_sec = int(seconds.get())
                seconds_total = (recommended_min * 60) + recommended_sec
                joule = recommended_pwr * seconds_total
                power_new = int(watt_new.get())
                seconds_total_new = joule / power_new
                seconds_modulus = round((seconds_total_new % 60))
                seconds_new.set(seconds_modulus)
                minutes_new.set(
                    round((seconds_total_new - seconds_modulus) / 60)
                    )
            except ValueError:
                root.bell()
                pass

        # Statements & variables.
        watt = StringVar()
        minutes = StringVar()
        seconds = StringVar()
        seconds.set(0)
        watt_new = StringVar()
        # Default power for own microwave.
        watt_new.set(750)
        minutes_new = StringVar()
        seconds_new = StringVar()

        # Frames.
        # Root frame.
        root_frame = ttk.Frame(
            root,
            padding='8 8 8 8'
            )
        root_frame.grid(
            column=0,
            row=0,
            sticky=(N, W, E, S)
            )
        # Recommended frame.
        recommended_frame = ttk.Labelframe(
            root_frame,
            text='Recommended:',
            padding='14 6 14 8'
            )
        recommended_frame.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky=(N, W, E, S)
            )
        # User's microwave frame.
        user_microwave_frame = ttk.Labelframe(
            root_frame,
            text='Your microwave:',
            padding='14 6 14 0'
            )
        user_microwave_frame.grid(
            column=0,
            row=1,
            sticky=W
            )
        # Calculation frame.
        calculation_frame = ttk.Frame(
            root_frame,
            padding='0 6 0 12'
            )
        calculation_frame.grid(
            column=0,
            row=3,
            columnspan=2,
            sticky=W
            )

        # Key binds and validation for input.
        root.bind('<Return>', calculator)
        root.bind('<KP_Enter>', calculator)
        validation = root_frame.register(only_numbers)

        # Calculation button.
        calc_button = ttk.Button(
            root_frame,
            text='Calculate',
            command=calculator
            )
        calc_button.grid(
            column=0,
            row=4,
            columnspan=2,
            sticky=(E, S, N, W)
            )

        # Watt text label.
        ttk.Label(
            recommended_frame,
            text='Watt'
            ).grid(
                column=0,
                row=0,
                sticky=W
                )
        # Watt entry (as suggested on package of TV dinner).
        watt_entry = ttk.Entry(
            recommended_frame,
            width=4,
            textvariable=watt,
            validate='key',
            validatecommand=(validation, '%S')
            )
        watt_entry.grid(
            column=0,
            row=1,
            sticky=W
            )
        watt_entry.focus()

        # Min text label.
        ttk.Label(
            recommended_frame,
            text='min.'
            ).grid(
                column=1,
                row=0,
                padx=5,
                sticky=W
                )
        # Minutes entry.
        minutes_entry = ttk.Entry(
            recommended_frame,
            width=3,
            textvariable=minutes,
            validate='key',
            validatecommand=(validation, '%S')
            )
        minutes_entry.grid(
            column=1,
            row=1,
            padx=5,
            sticky=W
            )

        # Sec text label.
        ttk.Label(
            recommended_frame,
            text='sec.'
            ).grid(
                column=2,
                row=0,
                sticky=W
                )
        # Seconds entry.
        seconds_entry = ttk.Entry(
            recommended_frame,
            width=2,
            textvariable=seconds,
            validate='key',
            validatecommand=(validation, '%S')
            )
        seconds_entry.grid(
            column=2,
            row=1,
            sticky=W
            )

        # Image label.
        ttk.Label(
            user_microwave_frame,
            image=imgobj
            ).grid(
                column=0,
                row=0,
                rowspan=2,
                sticky=W
                )
        # User's Watt text label.
        ttk.Label(
            user_microwave_frame,
            text='Watt'
            ).grid(
                column=1,
                row=0,
                padx=5,
                sticky=(W, S)
                )
        # User's Watt entry.
        watt_new_entry = ttk.Entry(
            user_microwave_frame,
            width=4,
            textvariable=watt_new,
            validate='key',
            validatecommand=(validation, '%S')
            )
        watt_new_entry.grid(
            column=1,
            row=1,
            padx=5,
            sticky=(W, N)
            )

        # Time text label.
        ttk.Label(
            calculation_frame,
            text='Time:'
            ).grid(
                column=0,
                row=0,
                sticky=W
                )
        # Calculated minutes.
        ttk.Label(
            calculation_frame,
            textvariable=minutes_new,
            font='-weight bold'
            ).grid(
                column=1,
                row=0,
                sticky=W
                )
        # Calculated min text label.
        ttk.Label(
            calculation_frame,
            text='min.'
            ).grid(
                column=2,
                row=0,
                sticky=W
                )
        # Calculated seconds.
        ttk.Label(
            calculation_frame,
            textvariable=seconds_new,
            font='-weight bold'
            ).grid(
                column=3,
                row=0,
                sticky=W
                )
        # Calculated sec text label.
        ttk.Label(
            calculation_frame,
            text='sec.'
            ).grid(
                column=4,
                row=0,
                sticky=W
                )


# Now, let's turn on the heat!
if __name__ == '__main__':
    root = Tk()
    root.title('Microwave')
    # Place window near the centre on the desktop.
    screen_width = str(int((root.winfo_screenwidth()) / 2 - 85))
    screen_height = str(int((root.winfo_screenheight()) / 2 - 200))
    desktop = '-' + screen_width + '+' + screen_height
    root.geometry(desktop)
    # Load and assign image.
    imgobj = BitmapImage(file='img/microwave.xbm', foreground='#555')
    app = App(root)
    root.mainloop()
