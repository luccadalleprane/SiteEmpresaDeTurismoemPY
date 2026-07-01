import flet as ft
import threading
import time

# =========================================================
# DADOS DAS VIAGENS FUTURAS
# =========================================================

viagens_futuras = [

    {
        "destino": "Porto Seguro",
        "data": "15 Julho 2026",
        "descricao": "Pacote completo com hotel e transporte.",
        "imagem": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },

    {
        "destino": "Gramado",
        "data": "02 Agosto 2026",
        "descricao": "Viagem de inverno com passeio turístico.",
        "imagem": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963"
    },

    {
        "destino": "Rio de Janeiro",
        "data": "20 Setembro 2026",
        "descricao": "Excursão com praia e city tour.",
        "imagem": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325"
    },

    {
        "destino": "Maceió",
        "data": "10 Outubro 2026",
        "descricao": "Praias paradisíacas.",
        "imagem": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
    },

    {
        "destino": "Recife",
        "data": "22 Novembro 2026",
        "descricao": "Passeios incríveis e praias.",
        "imagem": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
    },

    {
        "destino": "Salvador",
        "data": "15 Dezembro 2026",
        "descricao": "Cultura e diversão.",
        "imagem": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e"
    }

]

# =========================================================
# VIAGENS REALIZADAS
# =========================================================

viagens_realizadas = [

    {
        "nome": "Fernando de Noronha",

        "fotos": [

            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",

            "https://images.unsplash.com/photo-1493558103817-58b2924bce98",

            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"

        ]
    },

    {
        "nome": "Balneário Camboriú",

        "fotos": [

            "https://images.unsplash.com/photo-1493558103817-58b2924bce98",

            "https://images.unsplash.com/photo-1506744038136-46273834b3fb",

            "https://images.unsplash.com/photo-1470770841072-f978cf4d019e"

        ]
    },

    {
        "nome": "Arraial do Cabo",

        "fotos": [

            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

            "https://images.unsplash.com/photo-1483729558449-99ef09a8c325",

            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"

        ]
    },

    {
        "nome": "Florianópolis",

        "fotos": [

            "https://images.unsplash.com/photo-1506744038136-46273834b3fb",

            "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",

            "https://images.unsplash.com/photo-1516483638261-f4dbaf036963"

        ]
    }

]

# =========================================================
# CARD VIAGEM FUTURA
# =========================================================

class CardViagem(ft.Container):

    def __init__(self, viagem):

        super().__init__(

            width=260,
            height=360,

            bgcolor="white",

            border_radius=20,

            padding=15,

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color="#cccccc"
            ),

            content=ft.Column(

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                spacing=12,

                controls=[

                    ft.Image(
                        src=viagem["imagem"],
                        width=220,
                        height=150,
                        fit="cover",
                        border_radius=15
                    ),

                    ft.Text(
                        viagem["destino"],
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Text(
                        f"📅 {viagem['data']}",
                        size=16
                    ),

                    ft.Text(
                        viagem["descricao"],
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Container(expand=True),

                    ft.Button(
                        content=ft.Text(
                            "Reservar",
                            color="white"
                        ),
                        bgcolor="blue"
                    )

                ]
            )
        )

# =========================================================
# CARD VIAGEM REALIZADA
# =========================================================

class CardRealizada(ft.Container):

    def __init__(self, viagem, page):

        self.fotos = viagem["fotos"]

        self.index = 0

        self.page_ref = page

        self.imagem = ft.Image(
            src=self.fotos[0],
            width=340,
            height=220,
            fit="cover",
            border_radius=20
        )

        super().__init__(

            width=340,
            height=220,

            border_radius=20,

            margin=10,

            content=ft.Stack(

                controls=[

                    self.imagem,

                    ft.Container(

                        content=ft.Text(
                            viagem["nome"],
                            color="white",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
                        ),

                        bgcolor="#00000099",

                        padding=10,

                        border_radius=10,

                        bottom=10,
                        left=10,
                        right=10

                    )

                ]

            )

        )

        self.iniciar_slider()

    # =====================================================
    # TROCA AUTOMÁTICA DAS IMAGENS
    # =====================================================

    def iniciar_slider(self):

        def trocar():

            while True:

                time.sleep(8)

                self.index += 1

                if self.index >= len(self.fotos):
                    self.index = 0

                self.imagem.src = self.fotos[self.index]

                self.page_ref.update()

        threading.Thread(
            target=trocar,
            daemon=True
        ).start()

# =========================================================
# MAIN
# =========================================================

def main(page: ft.Page):

    page.title = "Aguia Toures"

    page.bgcolor = "#f3f5f7"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.scroll = ft.ScrollMode.AUTO

    page.window_width = 1500
    page.window_height = 900

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    conteudo = ft.Column(

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        spacing=25

    )

    indice_futuras = 0
    indice_realizadas = 0

    cards_futuras = ft.Row(
        spacing=25,
        alignment=ft.MainAxisAlignment.CENTER
    )

    cards_realizadas = ft.Row(
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # =====================================================
    # ATUALIZA FUTURAS
    # =====================================================

    def atualizar_futuras():

        cards_futuras.controls.clear()

        total = len(viagens_futuras)

        for i in range(4):

            index = (indice_futuras + i) % total

            cards_futuras.controls.append(
                CardViagem(viagens_futuras[index])
            )

        page.update()

    # =====================================================
    # ATUALIZA REALIZADAS
    # =====================================================

    def atualizar_realizadas():

        cards_realizadas.controls.clear()

        total = len(viagens_realizadas)

        for i in range(3):

            index = (indice_realizadas + i) % total

            cards_realizadas.controls.append(
                CardRealizada(
                    viagens_realizadas[index],
                    page
                )
            )

        page.update()

    # =====================================================
    # HOME
    # =====================================================

    def abrir_home(e=None):

        nonlocal indice_futuras
        nonlocal indice_realizadas

        conteudo.controls.clear()

        banner = ft.Container(

            width=min(page.window_width - 40, 1400),

            height=320,

            border_radius=25,

            image=ft.DecorationImage(
                src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                fit="cover"
            ),

            content=ft.Container(

                padding=40,

                content=ft.Column(

                    alignment=ft.MainAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "🌎 Aguia Toures",
                            size=45,
                            color="white",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            "Viaje para os melhores destinos do Brasil",
                            size=22,
                            color="white"
                        )

                    ]
                )
            )
        )

        conteudo.controls.append(banner)

        # =================================================
        # FUTURAS
        # =================================================

        conteudo.controls.append(

            ft.Text(
                "✈️ Próximas Viagens",
                size=38,
                weight=ft.FontWeight.BOLD
            )

        )

        atualizar_futuras()

        def esquerda_futuras(e):

            nonlocal indice_futuras

            indice_futuras -= 1

            atualizar_futuras()

        def direita_futuras(e):

            nonlocal indice_futuras

            indice_futuras += 1

            atualizar_futuras()

        conteudo.controls.append(

            ft.Row(

                alignment=ft.MainAxisAlignment.CENTER,

                vertical_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[

                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK_IOS,
                        icon_size=35,
                        on_click=esquerda_futuras
                    ),

                    cards_futuras,

                    ft.IconButton(
                        icon=ft.Icons.ARROW_FORWARD_IOS,
                        icon_size=35,
                        on_click=direita_futuras
                    )

                ]
            )
        )

        # =================================================
        # REALIZADAS
        # =================================================

        conteudo.controls.append(

            ft.Text(
                "📸 Viagens Realizadas",
                size=38,
                weight=ft.FontWeight.BOLD
            )

        )

        atualizar_realizadas()

        def esquerda_realizadas(e):

            nonlocal indice_realizadas

            indice_realizadas -= 1

            atualizar_realizadas()

        def direita_realizadas(e):

            nonlocal indice_realizadas

            indice_realizadas += 1

            atualizar_realizadas()

        conteudo.controls.append(

            ft.Row(

                alignment=ft.MainAxisAlignment.CENTER,

                vertical_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[

                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK_IOS,
                        icon_size=35,
                        on_click=esquerda_realizadas
                    ),

                    cards_realizadas,

                    ft.IconButton(
                        icon=ft.Icons.ARROW_FORWARD_IOS,
                        icon_size=35,
                        on_click=direita_realizadas
                    )

                ]
            )
        )

        page.update()

    # =====================================================
    # SOBRE
    # =====================================================

    def abrir_sobre(e=None):

        conteudo.controls.clear()

        conteudo.controls.append(

            ft.Container(

                width=min(page.window_width - 40, 1200),

                bgcolor="white",

                border_radius=25,

                padding=40,

                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="#cccccc"
                ),

                content=ft.Column(

                    spacing=20,

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "🏢 Sobre Nós",
                            size=40,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            "Somos especialistas em excursões e turismo pelo Brasil.",
                            size=22,
                            text_align=ft.TextAlign.CENTER
                        ),

                        ft.Text(
                            "Nossa missão é proporcionar experiências incríveis.",
                            size=20,
                            text_align=ft.TextAlign.CENTER
                        )

                    ]
                )
            )
        )

        page.update()

    # =====================================================
    # CONTATOS
    # =====================================================

    def abrir_contatos(e=None):

        conteudo.controls.clear()

        conteudo.controls.append(

            ft.Container(

                width=min(page.window_width - 40, 1000),

                bgcolor="white",

                border_radius=25,

                padding=40,

                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="#cccccc"
                ),

                content=ft.Column(

                    spacing=25,

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "📞 Contatos",
                            size=40,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            "📱 (27) 99999-9999",
                            size=22
                        ),

                        ft.Text(
                            "✉️ contato@horizonteturismo.com",
                            size=22
                        ),

                        ft.Text(
                            "📸 @horizonteturismo",
                            size=22
                        ),

                        ft.Text(
                            "📍 Castelo - ES",
                            size=22
                        )

                    ]
                )
            )
        )

        page.update()

    # =====================================================
    # MENU
    # =====================================================

    menu = ft.Container(

        width=min(page.window_width - 40, 1400),

        bgcolor="white",

        border_radius=20,

        padding=20,

        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color="#cccccc"
        ),

        content=ft.Row(

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

            vertical_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                ft.Text(
                    "🌎 Aguia Toures",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="blue"
                ),

                ft.Row(

                    spacing=15,

                    controls=[

                        ft.Button(
                            "HOME",
                            on_click=abrir_home
                        ),

                        ft.Button(
                            "SOBRE",
                            on_click=abrir_sobre
                        ),

                        ft.Button(
                            "CONTATOS",
                            on_click=abrir_contatos
                        )

                    ]
                )

            ]
        )
    )

    # =====================================================
    # ADICIONA NA TELA
    # =====================================================

    page.add(menu)

    page.add(
        ft.Container(height=20)
    )

    page.add(conteudo)

    abrir_home()

# =========================================================
# EXECUTA
# =========================================================

ft.app(target=main)