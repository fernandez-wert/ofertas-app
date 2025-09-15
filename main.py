from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Color de fondo más bonito
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class OfertasApp(App):
    def build(self):
        # Ofertas de ejemplo
        ofertas = [
            {"titulo": "💼 Desarrollador Python", "salario": "$2000", "empresa": "Tech Solutions"},
            {"titulo": "🎨 Diseñador UX/UI", "salario": "$1800", "empresa": "Creative Studio"},
            {"titulo": "📊 Analista de Datos", "salario": "$2200", "empresa": "Data Insights"},
            {"titulo": "🔧 Soporte Técnico", "salario": "$1500", "empresa": "IT Support"},
            {"titulo": "📱 Desarrollador Móvil", "salario": "$2100", "empresa": "App Masters"}
        ]
        
        layout_principal = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título
        titulo = Label(
            text="🎯 OFERTAS DE TRABAJO",
            size_hint_y=0.1,
            font_size='20sp',
            bold=True,
            color=(0.2, 0.4, 0.6, 1)
        )
        layout_principal.add_widget(titulo)
        
        # ScrollView para las ofertas
        scroll = ScrollView()
        contenedor_ofertas = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        contenedor_ofertas.bind(minimum_height=contenedor_ofertas.setter('height'))
        
        for oferta in ofertas:
            # Crear un botón para cada oferta
            btn = Button(
                text=f"{oferta['titulo']}\n"
                     f"🏢 {oferta['empresa']}\n"
                     f"💰 {oferta['salario']}",
                size_hint_y=None,
                height=120,
                background_color=(0.3, 0.6, 0.9, 1),
                color=(1, 1, 1, 1),
                font_size='16sp',
                halign='left',
                valign='center'
            )
            btn.bind(on_press=lambda instance, oferta=oferta: self.mostrar_detalles(oferta))
            contenedor_ofertas.add_widget(btn)
        
        scroll.add_widget(contenedor_ofertas)
        layout_principal.add_widget(scroll)
        
        return layout_principal
    
    def mostrar_detalles(self, oferta):
        print(f"Oferta seleccionada: {oferta['titulo']}")
        # Aquí puedes agregar más funcionalidad

# Ejecutar la aplicación
if __name__ == '__main__':
    OfertasApp().run()