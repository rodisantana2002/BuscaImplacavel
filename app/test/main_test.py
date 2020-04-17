import csv
import PySimpleGUI as sg


def main():
    # filename = os.path.join(os.path.expanduser('~'), 'Dropbox', 'Sync', 'inventarioHL.csv')
    filename = 'inventarioHL.csv'
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        header_list = next(reader)
        data = list(reader)  # read everything else into a list of rows
    sg.SetOptions(element_padding=(0, 10),
                  background_color='#F3F3F3')

    layout = [
        [sg.InputText(
            key='edit1',
            size=(50, 20),
            background_color='white',
            text_color='#2687FB',
            enable_events=True)],
        [sg.Table(
            key='table1',  # HELLO I EXIST
            values=data,
            headings=header_list,
            max_col_width=25,
            auto_size_columns=False,
            justification='left',
            background_color='#1DB954',  # Bg not changing color
            alternating_row_color='black',  # Colors are not changing
            # row_colors=''  # Any Examples on how to use this?
            num_rows=20,
            enable_events=True)],
        [sg.StatusBar(
            key='sb1',
            size=(137, 0),
            text='App Started!',
            text_color='red')]
    ]

    window = sg.Window(
        title='Table Example',
        return_keyboard_events=True,
        grab_anywhere=False).Layout(layout)

    while True:
        event, values = window.Read()

        if event is None or event == 'Exit':
            break

        if event == 'Escape:27':  # Exit on ESC
            window.close()

        # if event != 'Escape:27':
        #     window.Element('edit1').focus()  # I know this does not exist but how to manually focus on a widget?

        if event == 'Delete:46':  # Clear Edit1 on DEL
            window.Element('edit1').Update('')

        try:
            sb_update = window.FindElementWithFocus().Key
            print(window.FindElementWithFocus().Key)
        except:
            sb_update = window.FindElementWithFocus()
            print(window.FindElementWithFocus())

        window.Element('sb1').Update(f"Focused Key: {str(sb_update)} Event: {event} Value(s): {values}")

main()