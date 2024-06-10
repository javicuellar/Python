import investpy

#  Ejemplos en github:  https://github.com/alvarobartt/investpy

# recuperamos 10 acciones del Estados unidos
#   country:   United States, spain
pais = ["United States", "spain"]
df = investpy.get_stocks_overview(country=pais[1], n_results=500)
print(df)


#  Listado de paises con acciones
#print(investpy.get_stock_countries())
activo = ["bbva"]
#  Obtener información de un activo
df = investpy.get_stock_information(stock=activo[0], 
                                    country=pais[1], 
                                    as_json=True)
#  Entre la información que devuelve podemos analizar para posibles compras:
#       - media 52 semanas ->  '52 wk Range': '3.972-6.292'
#       - dividendo        ->  'Dividend (Yield)': '0.3101(6.31%)' 
#       -  'P/E Ratio': 5.16
#       -  '1-Year Change': '-13.38%'
#       -  'Prev. Close': 4.913
print(df)

print("  ----  Información de dividendos  ---- ")
df = investpy.get_stock_dividends(stock=activo[0], 
                                  country=pais[1])
print(df.head(6))

print("  ----  Acción resumen financiero  ----")
df = investpy.get_stock_financial_summary(stock=activo[0],
                                          country=pais[1], 
                                          summary_type='balance_sheet',
                                          period='annual')
print(df)


print(" ---  activos = stocks con nombre BBVA  ---")
df = investpy.search_stocks(by='name', value='BBVA')
print(df)

print(" ---- fondos = bonds de españa  ---")
df1 = investpy.get_funds(country=pais[1])
df2 = investpy.get_funds_list(country=pais[1])
print(df1)
print("Lista: \n",df2)


print(" ---  fondos = bonds con nombre BBVA  ---")
df = investpy.search_bonds(by='name', value='Bbva')
print(df)

print(" ---  fondos = bonds  --- ")
#df = investpy.get_bond_information(bond="fondo", as_json=False)
#print(df)

#  No funciona.... da error 403
exit()
df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')
print(df.head())


search_resultado = investpy.search_quotes(text ="apple", 
                                          products=["stocks"], 
                                          countries= ["united states"],
                                          n_results= 1)

print(search_resultado)
