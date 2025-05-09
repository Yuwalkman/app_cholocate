
import flet as ft
import datetime

class BakingInfo:
    time_info = ft.TextField(label = "Time") 
    tempeature_info = ft.TextField(label = " Temperature )", suffix_text="\u2103")

def main(page: ft.Page):
    
    bakingdeatil = BakingInfo()

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
    
    def check_info(e):
        ...

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

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [   ft.ElevatedButton(
                "Date Select",
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
                        ft.ElevatedButton("Next step", on_click=lambda _: page.go("/Example One")),
                        ft.AppBar(title=ft.Text("Roaster Info check "), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ],
                )
            )
        elif page.route == "/Example One":
            page.views.append(
                ft.View(
                    "/Example One",
                    [   bakingdeatil.time_info, bakingdeatil.tempeature_info,
                        ft.AppBar(title=ft.Text("Example One "), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Next Example ", on_click=lambda _: page.go("/Example Two")),
                    ],
                )
            )
       
        elif page.route == "/Example Two":
            page.views.append(
                ft.View(
                    "/Example Two",
                    [   bakingdeatil.time_info, bakingdeatil.tempeature_info,
                        ft.AppBar(title=ft.Text("Example Two "), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Next Example ", on_click=lambda _: page.go("/Example Three")),
                        ft.ElevatedButton("previous Example ", on_click=lambda _: page.go("/Example One")),
                    ],
                )
            )
        
        elif page.route == "/Example Three":
            page.views.append(
                ft.View(
                    "/Example Two",
                    [   bakingdeatil.time_info, bakingdeatil.tempeature_info,
                        ft.AppBar(title=ft.Text("Example Three "), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Next Example ", on_click=lambda _: page.go("/Example Four")),
                        ft.ElevatedButton("previous Example ", on_click=lambda _: page.go("/Example Three")),
                    ],
                )
            )

        page.update()
    
    page.on_route_change = route_change
    page.go("/")  # 设定起始页

ft.app(main)