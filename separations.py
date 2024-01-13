#Types of range (per day, per week, per pay(14 days, 15 days),per month)

def is_bis(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_splits(year, start_day, type_separation):
    if is_bis(year):
        total_days = 366 - start_day
    else:
        total_days = 365 - start_day
    
    separations, residual = divmod(total_days, type_separation)
    
    # Si hay un remanente de días, añadir una catorcena adicional
    if residual > 0:
        separations += 1
    
    return separations

# Año 2024
year = 2024

start_day = 8

type_separation = 14

# Calcular catorcenas
result_splits = calculate_splits(year, start_day, type_separation)

# Mostrar el resultado
print(f"El año {year} tiene {result_splits} catorcenas.")

