import PySimpleGUI as sg

def main():
    # Set a theme for the window (optional)
    sg.theme('DarkBlue')

    # Define the layout: a text prompt, a button, and a text element for output
    layout = [
        [sg.Text("Press the button to see a message:")],
        [sg.Button("Click Me", key='-BUTTON-')],
        [sg.Text("", key='-OUTPUT-', size=(20, 1))]
    ]

    # Create the window with the defined layout
    window = sg.Window("Simple UI Example", layout, finalize=True)

    # Event loop to process events (like button clicks)
    while True:
        event, values = window.read()
        # If user closes window, exit the loop
        if event == sg.WINDOW_CLOSED:
            break
        # If the button is clicked, update the output text
        elif event == '-BUTTON-':
            window['-OUTPUT-'].update("Nice booty")

    # Close the window when done
    window.close()

if __name__ == '__main__':
    main()

