salario_bruto = 5000
inss = 15
ir = 10
variavel_inss = (inss/100) * salario_bruto
variavel_ir = (ir/100) * variavel_inss
salario_liquido = salario_bruto - variavel_inss - variavel_ir
print(f"{variavel_inss}\n{variavel_ir}\n{salario_liquido}")

