from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class MeuApp(MDApp):
    def build(self):
        # Definindo o tema para roxo (estilo moderno)
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        
        screen = MDScreen()

        # Barra de ferramentas superior
        toolbar = MDTopAppBar(title="Meu App Independente", pos_hint={"top": 1})
        toolbar.elevation = 4
        screen.add_widget(toolbar)

        # Texto central
        screen.add_widget(
            MDLabel(
                text="O Termux não precisa estar aberto!",
                halign="center",
                pos_hint={"center_y": 0.6},
                theme_text_color="Secondary"
            )
        )

        # Botão de ação
        screen.add_widget(
            MDRaisedButton(
                text="TESTAR HARDWARE",
                pos_hint={"center_x": 0.5, "center_y": 0.4},
                on_release=self.acao_botao
            )
        )
        
        return screen

    def acao_botao(self, instance):
        print("Botão pressionado! No APK, isso pode vibrar ou abrir a câmera.")
        instance.text = "FUNCIONANDO!"

if __name__ == "__main__":
    MeuApp().run()
