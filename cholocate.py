import datetime
import flet as ft


def main(page: ft.Page):
    page.window_width = 375  # iPhone 标准宽度
    page.window_height = 812  # iPhone 高度（带刘海）
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.padding = 16  # 适合触摸操作的间距
    page.scroll = ft.ScrollMode.AUTO  # 允许滚动

    t = ft.Text()
    tb1 = ft.TextField(label = "Roaster Name ")
    tb2 = ft.TextField(label = " Room Temperature )", suffix_text="\u2103")
    tb3 = ft.TextField(label = "Beans Origin ")
    tb4 = ft.TextField(label = " Date ",read_only=True)
    result_label = ft.Text("", color="black")
    
    def roaster_info(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}',{tb4.value},"
        page.update()
    
    def handle_change(e):
        if e.control.value:
            new_text = f"{e.control.value.strftime('%m/%d/%Y')}"
            tb4.value = new_text
            tb4.update()  # 更新文本内容

    def handle_dismissal(e):
        if e.control.value == None :
            new_text = f" Please select the date "
            tb4.value = new_text
            tb4.update()

    page.add(
        ft.ElevatedButton(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2000, month=10, day=1),
                    last_date=datetime.datetime(year=2025, month=10, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
        ),
        tb4,tb1,tb2,tb3,
        ft.ElevatedButton("Submit", on_click=roaster_info),
    )
ft.app(main)