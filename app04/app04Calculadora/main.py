import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
        def calc_resta(txtNum1,txtNum2,lblResultado):
        
        
        
def main(page: ft.Page):
    page.tittle="Calculadora"
    page.bgcolor="green"
    
    txtNum1=ft.TextField(label="ingresa el primer numero",color="yellow")
    txtNum2=ft.TextField(label="ingresa el segundo numero",color="yellow")
    lblResultado=ft.TextField("Resultado: ",color="yellow")
    
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_click=on_calc_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click=on_calc_division)
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
            ],alignment="center"),
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            BtnMultiplicacion,
            btnDivision
        ],alignment="center")
    )


ft.app(main)
