import flet as ft

click = 0

def main(page):
    def on_click(e):
        global click
        click += 1
        t.value = f"{click}"
        page.update()

    def on_reset(e):
        global click
        click = 0
        t.value = "0"
        page.update()

    def on_save(e):
        with open('click_count.txt', 'w') as file:
            file.write(str(click))
        t1 = ft.Text("Click count saved successfully!")
        page.add(t1)

    a = ft.ElevatedButton(text="Click Me", on_click=on_click)
    reset = ft.ElevatedButton(text="Reset", on_click=on_reset)
    save = ft.ElevatedButton(text="Save", on_click=on_save)
    t = ft.Text(value="0")

    page.add(a, reset, save, t)

ft.app(target=main)


