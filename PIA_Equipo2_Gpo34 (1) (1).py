import math
'''
DATOS A USAR
TABLA 1
13000
500
20000
420
14500
380
12800
310
8000
195
6500
250

TABLA 3
20000
5500
9500
8500
5000
4000

TABLA 4
#SE REPITE 3 VECES
1.2
0.4
12.0
1.7
0.6
24.0
2.0
1.2
5.0

TABLA 5
8000 
8000 
12
8000 
4000
13
8000 
4000
2000
2000
2
2000
3500
4
2000
3500
1000
1000
2
1000
2800
3
1000
2800

TABLA 7
3.0
16
3.0
20
3.0
1.5
16
1.5
20
1.5
2.0
16
2.0
20
2.0

TABLA 8
45000
12000
43000
50000
15000
45000
12000
35000
38000
15000

TABLA 9
7000
140000
10000
3500
7000
140000
8000
3500

TABLA 10
1.70
0.40
12
1.70
.80
24
1
1.50
2.50
1.20
6
2

TABLA II presupuesto
45000
140000

TABLA Estado de Flujo de Efectivo
200000
85000

TABLA Balance general
35000
10500
900000
98000
140000
1900000
32000

'''
#ACTIVOS 
FluEfectActual=200000
SaldoClientes=90000
DD=35000
IFM=45000
FM=10500
IFPT=140000
MT=900000
BPYE=1600000
DAC=-750000
#PASIVOS
SPT20=50500
DP=98000
ISRxPg=50000
PB=140000
#CAPITALCONTABLE
CA=1900000
CG=32000

ISR2021=0
ISR2020=50000

print("BIENVENIDO AL PROGRAMA PRESUPUESTO MAESTRO \n")
#TABLA 1
while(True):
    try:
        print("-------PRESUPUESTO MAESTRO-------")
        print("\nMadererias Mexicanas S.A de C.V.")
        print("\nDentro de sus operaciones del 2020 fabrica tres estilos de muebles:")
        print("\nMC Mueble Comedor, MS Mueble Sala y MR Mueble Ropero")
        print("\nI. Presupuesto de Operación.")
        print("\nP1: PRODUCTO MC")
        Us1P1=int(input("\nIngrese las unidades a vender del primer semestre P1:"))
        Ps1P1=int(input("Ingrese el precio de venta del primer semestre P1:"))
        Us2P1=int(input("Ingrese las unidades a vender del segundo semestre P1:"))
        Ps2P1=int(input("Ingrese el precio de venta del segundo semestre P1:"))
        print("\nP2: PRODUCTO MS")
        Us1P2=int(input("\nIngrese las unidades a vender del primer semestre P2:"))
        Ps1P2=int(input("Ingrese el precio de venta del primer semestre P2:"))
        Us2P2=int(input("Ingrese las unidades a vender del segundo semestre P2:"))
        Ps2P2=int(input("Ingrese el precio de venta del segundo semestre P2:"))
        print("\nP3: PRODUCTO MR")
        Us1P3=int(input("\nIngrese las unidades a vender del primer semestre P3:"))
        Ps1P3=int(input("Ingrese el precio de venta del primer semestre P3:"))
        Us2P3=int(input("Ingrese las unidades a vender del segundo semestre P3:"))
        Ps2P3=int(input("Ingrese el precio de venta del segundo semestre P3:"))
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
#OPERACIONES
#TABLA 1
IVs1p1=Us1P1*Ps1P1
IVs2p1=Us2P1*Ps2P1
ImA1=IVs1p1+IVs2p1
IVs1p2=Us1P2*Ps1P2
IVs2p2=Us2P2*Ps2P2
ImA2=IVs1p2+IVs2p2
IVs1p3=Us1P3*Ps1P3
IVs2p3=Us2P3*Ps2P3
ImA3=IVs1p3+IVs2p3
TVS1=IVs1p1+IVs1p2+IVs1p3
TVS2=IVs2p1+IVs2p2+IVs2p3
TVA=ImA1+ImA2+ImA3
#TABLA 2
TClientes2021=SaldoClientes+TVA
Cobranza2021=TVA*0.8
TEntradas2021=SaldoClientes+Cobranza2021
STClientes2021=TClientes2021-TEntradas2021
#--------------------------------------------------------------------------------------------

print("\n-------PRESUPUESTO MAESTRO-------")
print("\nMadererias Mexicanas S.A de C.V.")
print("\nI. Presupuesto de Operación.")
print("-"*89)
print("|1. Presupuesto de Ventas.\t \t \t\t\t \t\t\t|")
print("-"*89)
print("|\tPRODUCTOS \t|\t1er Semestre\t|\t 2do Semestre \t|\t 2021\t|")
print("-"*89)
print("|\tPRODUCTO MC\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a vender\t|\t{Us1P1}\t\t|\t{Us2P1}\t\t|\t  \t|")
print("-"*89)
print(f"|Precio de Venta  \t|\t{Ps1P1}\t\t|\t{Ps2P1}\t\t|\t  \t|")
print("-"*89)
print(f"|Importe de Venta \t|\t{IVs1p1}\t\t|\t{IVs2p1}\t\t|\t{ImA1}|")
print("-"*89)
print("|\tPRODUCTO MS\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a vender\t|\t{Us1P2}\t\t|\t{Us2P2}\t\t|\t  \t|")
print("-"*89)
print(f"|Precio de Venta  \t|\t{Ps1P2}\t\t|\t{Ps2P2}\t\t|\t  \t|")
print("-"*89)
print(f"|Importe de Venta \t|\t{IVs1p2}\t\t|\t{IVs2p2}\t\t|\t{ImA2}\t|")
print("-"*89)
print("|\tPRODUCTO MR\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a vender\t|\t{Us1P3}\t\t|\t{Us2P3}\t\t|\t  \t|")
print("-"*89)
print(f"|Precio de Venta  \t|\t{Ps1P3}\t\t|\t{Ps2P3}\t\t|\t  \t|")
print("-"*89)
print(f"|Importe de Venta \t|\t{IVs1p3}\t\t|\t{IVs2p3}\t\t|\t{ImA3}\t|")
print("-"*89)
print(f"|Total de Venta por Sem |\t{TVS1}\t|\t{TVS2}\t|\t{TVA}|")
print("-"*89)

#--------------------------------------------------------------------------------------------

print("\n")
print("-"*89)
print("|2. Determinación del saldo de Clientes y Flujo de Entradas\t \t\t\t|")
print("-"*89)
print("|\t Descripción\t\t\t|\t Importe\t|\t  Total  \t|")
print("-"*89)
print(f"|\t Saldo de clientes 31-Dic-2020 \t|\t\t\t|\t{SaldoClientes}\t\t|")
print("-"*89)
print(f"|\tVentas 2021\t\t\t|\t\t\t|\t {TVA} \t|")
print("-"*89)
print(f"|\t Total de Clientes 2021 \t|\t\t\t|\t {TClientes2021} \t|")
print("-"*89)
print("|\t Entradas de Efectivo: \t\t|\t\t\t|\t\t\t|")
print("-"*89)
print(f"|\t Por Cobranza del 2020\t\t|\t  {SaldoClientes}  \t|\t\t\t|")
print("-"*89)
print(f"|\t Por Cobranza del 2021\t\t|\t{Cobranza2021}\t|\t\t\t|")
print("-"*89)
print(f"|\t Total de entradas del 2021\t|\t\t\t|\t{TEntradas2021}\t|")
print("-"*89)
print(f"|\t Saldo de Clientes del 2021\t|\t\t\t|\t {STClientes2021} \t|")
print("-"*89)
print("\n")

#--------------------------------------------------------------------------------------------
#TABLA 3
while(True):
    try:
        print("\nMadererias Mexicanas S.A de C.V.")
        print("\n3. Presupuesto de Producción.")
        InvInicialS1P1=int(input("Ingresa el inventario inicial Producto 1: "))
        InvFinalS2P1=int(input("Ingresa el inventario final Producto 1: "))
        InvInicialS1P2=int(input("Ingresa el inventario inicial Producto 2: "))
        InvFinalS2P2=int(input("Ingresa el inventario final Producto 2: "))
        InvInicialS1P3=int(input("Ingresa el inventario inicial Producto 3: "))
        InvFinalS2P3=int(input("Ingresa el inventario final Producto 3: "))
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
#OPERACIONES
#P1
TUnidadesS1P1=Us1P1+InvInicialS1P1
UniProducirS1P1=TUnidadesS1P1-InvInicialS1P1
TUnidadesS2P1=Us2P1+InvFinalS2P1
UniProducirS2P1=TUnidadesS2P1-InvInicialS1P1
#P2
TUnidadesS1P2=Us1P2+InvInicialS1P2
UniProducirS1P2=TUnidadesS1P2-InvInicialS1P2
TUnidadesS2P2=Us2P2+InvFinalS2P2
UniProducirS2P2=TUnidadesS2P2-InvInicialS1P2
#P3
TUnidadesS1P3=Us1P3+InvInicialS1P3
UniProducirS1P3=TUnidadesS1P3-InvInicialS1P3
TUnidadesS2P3=Us2P3+InvFinalS2P3
UniProducirS2P3=TUnidadesS2P3-InvInicialS1P3
#Total 2016
T2021UniVender=Us1P1+Us2P1
T2021Unidades=T2021UniVender+InvFinalS2P1
T2021UniProdP1=T2021Unidades-InvInicialS1P1

T2021UniVender2=Us1P2+Us2P2
T2021Unidades2=T2021UniVender2+InvFinalS2P2
T2021UniProdP2=T2021Unidades2-InvInicialS1P2

T2021UniVender3=Us1P3+Us2P3
T2021Unidades3=T2021UniVender3+InvFinalS2P3
T2021UniProdP3=T2021Unidades3-InvInicialS1P3

print("\n")
print("-"*81)
print("|3. Presupuesto de Producción\t \t\t\t\t\t\t|")
print("-"*81)
print("|\t\t\t\t|  1er Semestre |  2do Semestre |  Total 2021  |")
print("-"*81)
print("|\tPRODUCTO MC\t\t|\t\t|\t\t|\t\t|")
print("-"*81)
print(f"|\t Unidades a vender \t|\t{Us1P1}\t|\t{Us2P1}\t|\t{T2021UniVender}\t|")
print("-"*81)
print(f"|\t(+) Inventario Final\t|\t{InvInicialS1P1}\t|\t{InvFinalS2P1}\t|\t{InvFinalS2P1}\t|")
print("-"*81)
print(f"|\t(=) Total de Unidades\t|\t{TUnidadesS1P1}\t|\t{TUnidadesS2P1}\t|\t{T2021Unidades}\t|")
print("-"*81)
print(f"|\t(-) Inventario Inicial\t|\t{InvInicialS1P1}\t|\t{InvInicialS1P1}\t|\t{InvInicialS1P1}\t|")
print("-"*81)
print(f"|\t(=) Unidades a Producir\t|\t{UniProducirS1P1}\t|\t{UniProducirS2P1}\t|\t{T2021UniProdP1}\t|")
print("-"*81)
print("|\tPRODUCTO MS\t\t|\t\t|\t\t|\t\t|")
print("-"*81)
print(f"|\tUnidades a vender\t|\t{Us1P2}\t|\t{Us2P2}\t|\t{T2021UniVender2}\t|")
print("-"*81)
print(f"|\t(+) Inventario Final\t|\t{InvInicialS1P2}\t|\t{InvFinalS2P2}\t|\t{InvFinalS2P2}\t|")
print("-"*81)
print(f"|\t(=) Total de Unidades\t|\t{TUnidadesS1P2}\t|\t{TUnidadesS2P2}\t|\t{T2021Unidades2}\t|")
print("-"*81)
print(f"|\t(-) Inventario Inicial\t|\t{InvInicialS1P2}\t|\t{InvInicialS1P2}\t|\t{InvInicialS1P2}\t|")
print("-"*81)
print(f"|\t(=) Unidades a Producir\t|\t{UniProducirS1P2}\t|\t{UniProducirS2P2}\t|\t{T2021UniProdP2}\t|")
print("-"*81)
print("|\tPRODUCTO MR\t\t|\t\t|\t\t|\t\t|")
print("-"*81)
print(f"|\tUnidades a vender\t|\t{Us1P3}\t|\t{Us2P3}\t|\t{T2021UniVender3}\t|")
print("-"*81)
print(f"|\t(+) Inventario Final\t|\t{InvInicialS1P3}\t|\t{InvFinalS2P3}\t|\t{InvFinalS2P3}\t|")
print("-"*81)
print(f"|\t(=) Total de Unidades\t|\t{TUnidadesS1P3}\t|\t{TUnidadesS2P3}\t|\t{T2021Unidades3}\t|")
print("-"*81)
print(f"|\t(-) Inventario Inicial\t|\t{InvInicialS1P3}\t|\t{InvInicialS1P3}\t|\t{InvInicialS1P3}\t|")
print("-"*81)
print(f"|\t(=) Unidades a Producir\t|\t{UniProducirS1P3}\t|\t{UniProducirS2P3}\t|\t{T2021UniProdP3}\t|")
print("-"*81)
#--------------------------------------------------------------------------------------------
while(True):
    try:
        print("\n4. Presupuesto de Requerimiento de Materiales.")
        print("\nP1: PRODUCTO MC")
        print("MATERIAL A")
        RMAS1P1=float(input("Ingrese el Requerimiento de material del material A del semestre 1:"))
        RMAS2P1=float(input("Ingrese el Requerimiento de material del material A del semestre 2:"))
        RMA21P1=float(input("Ingrese el Requerimiento de material del material A anual:"))
        print("MATERIAL B")
        RMBS1P1=float(input("Ingrese el Requerimiento de material del material B del semestre 1:"))
        RMBS2P1=float(input("Ingrese el Requerimiento de material del material B del semestre 2:"))
        RMB21P1=float(input("Ingrese el Requerimiento de material del material B anual:"))
        print("MATERIAL C")
        RMCS1P1=float(input("Ingrese el Requerimiento de material del material C del semestre 1:"))
        RMCS2P1=float(input("Ingrese el Requerimiento de material del material C del semestre 2:"))
        RMC21P1=float(input("Ingrese el Requerimiento de material del material C anual:"))

        print("\nP2: PRODUCTO MS")
        print("MATERIAL A")
        RMAS1P2=float(input("Ingrese el Requerimiento de material del material A del semestre 1:"))
        RMAS2P2=float(input("Ingrese el Requerimiento de material del material A del semestre 2:"))
        RMA21P2=float(input("Ingrese el Requerimiento de material del material A anual:"))
        print("MATERIAL B")
        RMBS1P2=float(input("Ingrese el Requerimiento de material del material B del semestre 1:"))
        RMBS2P2=float(input("Ingrese el Requerimiento de material del material B del semestre 2:"))
        RMB21P2=float(input("Ingrese el Requerimiento de material del material B anual:"))
        print("MATERIAL C")
        RMCS1P2=float(input("Ingrese el Requerimiento de material del material C del semestre 1:"))
        RMCS2P2=float(input("Ingrese el Requerimiento de material del material C del semestre 2:"))
        RMC21P2=float(input("Ingrese el Requerimiento de material del material C anual:"))

        print("\nP3: PRODUCTO MR")
        print("MATERIAL A")
        RMAS1P3=float(input("Ingrese el Requerimiento de material del material A del semestre 1:"))
        RMAS2P3=float(input("Ingrese el Requerimiento de material del material A del semestre 2:"))
        RMA21P3=float(input("Ingrese el Requerimiento de material del material A anual:"))
        print("MATERIAL B")
        RMBS1P3=float(input("Ingrese el Requerimiento de material del material B del semestre 1:"))
        RMBS2P3=float(input("Ingrese el Requerimiento de material del material B del semestre 2:"))
        RMB21P3=float(input("Ingrese el Requerimiento de material del material B anual:"))
        print("MATERIAL C")
        RMCS1P3=float(input("Ingrese el Requerimiento de material del material C del semestre 1:"))
        RMCS2P3=float(input("Ingrese el Requerimiento de material del material C del semestre 2:"))
        RMC21P3=float(input("Ingrese el Requerimiento de material del material C anual:"))
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
#PRODUCTO1
TRMAS1P1=RMAS1P1*UniProducirS1P1
TRMBS1P1=RMBS1P1*UniProducirS1P1
TRMCS1P1=RMCS1P1*UniProducirS1P1
TRMAS2P1=RMAS2P1*UniProducirS2P1
TRMBS2P1=RMBS2P1*UniProducirS2P1
TRMCS2P1=RMCS2P1*UniProducirS2P1
TRMA21P1=RMA21P1*T2021UniProdP1
TRMB21P1=RMB21P1*T2021UniProdP1
TRMC21P1=RMC21P1*T2021UniProdP1
#PRODUCTO2
TRMAS1P2=RMAS1P2*UniProducirS1P2
TRMBS1P2=RMBS1P2*UniProducirS1P2
TRMCS1P2=RMCS1P2*UniProducirS1P2
TRMAS2P2=RMAS2P2*UniProducirS2P2
TRMBS2P2=RMBS2P2*UniProducirS2P2
TRMCS2P2=RMCS2P2*UniProducirS2P2
TRMA21P2=RMA21P2*T2021UniProdP2
TRMB21P2=RMB21P2*T2021UniProdP2
TRMC21P2=RMC21P2*T2021UniProdP2
#PRODUCTO3
TRMAS1P3=RMAS1P3*UniProducirS1P3
TRMBS1P3=RMBS1P3*UniProducirS1P3
TRMCS1P3=RMCS1P3*UniProducirS1P3
TRMAS2P3=RMAS2P3*UniProducirS2P3
TRMBS2P3=RMBS2P3*UniProducirS2P3
TRMCS2P3=RMCS2P3*UniProducirS2P3
TRMA21P3=RMA21P3*T2021UniProdP3
TRMB21P3=RMB21P3*T2021UniProdP3
TRMC21P3=RMC21P3*T2021UniProdP3
#TOTAL DE REQUERIMIENTOS EN GRAMOS
TRGMAS1=TRMAS1P1+TRMAS1P2+TRMAS1P3
TRGMAS2=TRMAS2P1+TRMAS2P2+TRMAS2P3
TRGMA21=TRMA21P1+TRMA21P2+TRMA21P3
TRGMBS1=TRMBS1P1+TRMBS1P2+TRMBS1P3
TRGMBS2=TRMBS2P1+TRMBS2P2+TRMBS2P3
TRGMB21=TRMB21P1+TRMB21P2+TRMB21P3
TRGMCS1=TRMCS1P1+TRMCS1P2+TRMCS1P3
TRGMCS2=TRMCS2P1+TRMCS2P2+TRMCS2P3
TRGMC21=TRMC21P1+TRMC21P2+TRMC21P3
print("\n")
print("-"*89)
print("|4. Presupuesto de Requerimiento de Materiales\t\t\t\t\t\t|")
print("-"*89)
print("|\tPRODUCTOS \t|\t1er Semestre\t|\t 2do Semestre \t|\t 2021\t|")
print("-"*89)
print("|\tPRODUCTO MC\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a vender\t|\t{UniProducirS1P1}\t\t|\t{UniProducirS2P1}\t\t|\t{T2021UniProdP1}\t|")
print("-"*89)
print("|\tMATERIAL A\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMAS1P1}\t\t|\t{RMAS2P1}\t\t|\t{RMA21P1}\t|")
print("-"*89)
print(f"|Total de Material A req|\t{TRMAS1P1}\t\t|\t{TRMAS2P1}\t\t|\t{TRMA21P1}\t|")
print("-"*89) 
print("|\tMATERIAL B\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMBS1P1}\t\t|\t{RMBS2P1}\t\t|\t{RMB21P1}\t|")
print("-"*89)
print(f"|Total de Material B req|\t{TRMBS1P1}\t\t|\t{TRMBS2P1}\t\t|\t{TRMB21P1}\t|")
print("-"*89)
print("|\tMATERIAL C\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMCS1P1}\t\t|\t{RMCS2P1}\t\t|\t{RMC21P1}\t|")
print("-"*89)
print(f"|Total de Material C req|\t{TRMCS1P1}\t|\t{TRMCS2P1}\t\t|\t{TRMC21P1}|")
print("-"*89)
print("|\tPRODUCTO MS\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a vender\t|\t{UniProducirS1P2}\t\t|\t{UniProducirS2P2}\t\t|\t{T2021UniProdP2}\t|")
print("-"*89)
print("|\tMATERIAL A\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMAS1P2}\t\t|\t{RMAS2P2}\t\t|\t{RMA21P2}\t|")
print("-"*89)
print(f"|Total de Material A req|\t{TRMAS1P2}\t\t|\t{TRMAS2P2}\t\t|\t{TRMA21P2}\t|")
print("-"*89) 
print("|\tMATERIAL B\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMBS1P2}\t\t|\t{RMBS2P2}\t\t|\t{RMB21P2}\t|")
print("-"*89)
print(f"|Total de Material B req|\t{TRMBS1P2}\t\t|\t{TRMBS2P2}\t\t|\t{TRMB21P2}\t|")
print("-"*89)
print("|\tMATERIAL C\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMCS1P2}\t\t|\t{RMCS2P2}\t\t|\t{RMC21P2}\t|")
print("-"*89)
print(f"|Total de Material C req|\t{TRMCS1P2}\t|\t{TRMCS2P2}\t|\t{TRMC21P2}|")
print("-"*89)
print("|\tPRODUCTO MR\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a vender\t|\t{UniProducirS1P3}\t\t|\t{UniProducirS2P3}\t\t|\t{T2021UniProdP3}\t|")
print("-"*89)
print("|\tMATERIAL A\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMAS1P3}\t\t|\t{RMAS2P3}\t\t|\t{RMA21P3}\t|")
print("-"*89)
print(f"|Total de Material A req|\t{TRMAS1P3}\t\t|\t{TRMAS2P3}\t\t|\t{TRMA21P3}\t|")
print("-"*89) 
print("|\tMATERIAL B\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMBS1P3}\t\t|\t{RMBS2P3}\t\t|\t{RMB21P3}\t|")
print("-"*89)
print(f"|Total de Material B req|\t{TRMBS1P3}\t\t|\t{TRMBS2P3}\t\t|\t{TRMB21P3}\t|")
print("-"*89)
print("|\tMATERIAL C\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{RMCS1P3}\t\t|\t{RMCS2P3}\t\t|\t{RMC21P3}\t|")
print("-"*89)
print(f"|Total de Material C req|\t{TRMCS1P3}\t\t|\t{TRMCS2P3}\t\t|\t{TRMC21P3}\t|")
print("-"*89)
print("|Total de Requerimientos (gramos)\t\t\t\t\t\t\t|")
print("-"*89)
print(f"|\tMATERIAL A\t|\t{TRGMAS1}\t\t|\t{TRGMAS2}\t\t|\t{TRGMA21}\t|")
print("-"*89)
print(f"|\tMATERIAL B\t|\t{TRGMBS1}\t\t|\t{TRGMBS2}\t\t|\t{TRGMB21}\t|")
print("-"*89)
print(f"|\tMATERIAL C\t|\t{TRGMCS1}\t|\t{TRGMCS2}\t|\t{TRGMC21}|")
print("-"*89)
print("\n")
#--------------------------------------------------------------------------------------------
#5. PRESUPUESTO DE COMPRA DE MATERIALES
while(True):
    try:
        print("\n5. PRESUPUESTO DE COMPRA DE MATERIALES.")
        print("MATERIAL A")
        IIMAS1=int(input("Ingrese el Inventario Inicial Material A del primer semestre: "))
        IFMAS1=int(input("Ingrese el Inventario Final Material A del primer semestre: "))
        PCMAS1=int(input("Ingrese el precio de compra del Material A del primer semestre: "))
        IIMAS2=int(input("Ingrese el Inventario Inicial Material A del segundo semestre: "))
        IFMAS2=int(input("Ingrese el Inventario Final Material A del segundo semestre: "))
        PCMAS2=int(input("Ingrese el precio de compra del Material A del segundo semestre:  "))
        IIMA21=int(input("Ingrese el Inventario Inicial Material A anual: "))
        IFMA21=int(input("Ingrese el Inventario Final Material A anual: "))
        print("\nMATERIAL B")
        IIMBS1=int(input("Ingrese el Inventario Inicial Material B del primer semestre: "))
        IFMBS1=int(input("Ingrese el Inventario Final Material B del primer semestre: "))
        PCMBS1=int(input("Ingrese el precio de compra del Material B del primer semestre: "))
        IIMBS2=int(input("Ingrese el Inventario Inicial Material B del segundo semestre: "))
        IFMBS2=int(input("Ingrese el Inventario Final Material B del segundo semestre: "))
        PCMBS2=int(input("Ingrese el precio de compra del Material B del segundo semestre:  "))
        IIMB21=int(input("Ingrese el Inventario Inicial Material B anual: "))
        IFMB21=int(input("Ingrese el Inventario Final Material B anual: "))
        print("\nMATERIAL C")
        IIMCS1=int(input("Ingrese el Inventario Inicial Material C del primer semestre: "))
        IFMCS1=int(input("Ingrese el Inventario Final Material C del primer semestre: "))
        PCMCS1=int(input("Ingrese el precio de compra del Material C del primer semestre: "))
        IIMCS2=int(input("Ingrese el Inventario Inicial Material C del segundo semestre: "))
        IFMCS2=int(input("Ingrese el Inventario Final Material C del segundo semestre: "))
        PCMCS2=int(input("Ingrese el precio de compra del Material C del segundo semestre:  "))
        IIMC21=int(input("Ingrese el Inventario Inicial Material C anual: "))
        IFMC21=int(input("Ingrese el Inventario Final Material C anual: "))
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
#
TTMAS1=TRGMAS1+IFMAS1
TTMAS2=TRGMAS2+IFMAS2
TTMA21=TRGMA21+IFMA21
MCMAS1=TTMAS1-IIMAS1
MCMAS2=TTMAS2-IIMAS2
MCMA21=TTMA21-IIMA21
TMAPS1=MCMAS1*PCMAS1
TMAPS2=MCMAS2*PCMAS2
TMAP21=TMAPS1+TMAPS2
TTMBS1=TRGMBS1+IFMBS1
TTMBS2=TRGMBS2+IFMBS2
TTMB21=TRGMB21+IFMB21
MCMBS1=TTMBS1-IIMBS1
MCMBS2=TTMBS2-IIMBS2
MCMB21=TTMB21-IIMB21
TMBPS1=MCMBS1*PCMBS1
TMBPS2=MCMBS2*PCMBS2
TMBP21=TMBPS1+TMBPS2
TTMCS1=TRGMCS1+IFMCS1
TTMCS2=TRGMCS2+IFMCS2
TTMC21=TRGMC21+IFMC21
MCMCS1=TTMCS1-IIMCS1
MCMCS2=TTMCS2-IIMCS2
MCMC21=TTMC21-IIMC21
TMCPS1=MCMCS1*PCMCS1
TMCPS2=MCMCS2*PCMCS2
TMCP21=TMCPS1+TMCPS2
CTS1=TMAPS1+TMBPS1+TMCPS1
CTS2=TMAPS2+TMBPS2+TMCPS2
CT21=TMAP21+TMBP21+TMCP21

print("-"*89)
print("|5. Presupuesto de Compra de Materiales\t\t\t\t\t\t\t|")
print("-"*89)
print("|\tPRODUCTOS  \t|\t1er Semestre\t|\t 2do Semestre \t|\t 2021\t|")
print("-"*89)
print("|\tMATERIAL A \t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{TRGMAS1}\t\t|\t{TRGMAS2}\t\t|\t{TRGMA21}\t|")
print("-"*89)
print(f"|( + ) Inventario Final |\t{IFMAS1}\t\t|\t{IFMAS2}\t\t|\t{IFMA21}\t|")
print("-"*89)
print(f"|Total de Materiales    |\t{TTMAS1}\t\t|\t{TTMAS2}\t\t|\t{TTMA21}\t|")
print("-"*89)
print(f"|( + ) Inventario Final |\t{IIMAS1}\t\t|\t{IIMAS2}\t\t|\t{IIMA21}\t|")
print("-"*89)
print(f"|Material a comprar     |\t{MCMAS1}\t\t|\t{MCMAS2}\t\t|\t{MCMA21}\t|")
print("-"*89)
print(f"|Precio de Compra:      |\t{PCMAS1}\t\t|\t{PCMAS2}\t\t|\t  \t|")
print("-"*89)
print(f"|Total MaterialA en $   |\t{TMAPS1}\t|\t{TMAPS2}\t| {TMAP21}\t|")
print("-"*89)
print("|\tMATERIAL B\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{TRGMBS1}\t\t|\t{TRGMBS2}\t\t|\t{TRGMB21}\t|")
print("-"*89)
print(f"|( + ) Inventario Final |\t{IFMBS1}\t\t|\t{IFMBS2}\t\t|\t{IFMB21}\t|")
print("-"*89)
print(f"|Total de Materiales:   |\t{TTMBS1}\t\t|\t{TTMBS2}\t\t|\t{TTMB21}\t|")
print("-"*89)
print(f"|( + ) Inventario Final |\t{IIMBS1}\t\t|\t{IIMBS2}\t\t|\t{IIMB21}\t|")
print("-"*89)
print(f"|Material a comprar:    |\t{MCMBS1}\t\t|\t{MCMBS2}\t\t|\t{MCMB21}\t|")
print("-"*89)
print(f"|Precio de Compra:      |\t{PCMBS1}\t\t|\t{PCMBS2}\t\t|\t  \t|")
print("-"*89)
print(f"|Total MaterialB en $:  |\t{TMBPS1}\t\t|\t{TMBPS2}\t\t|\t{TMBP21}|")
print("-"*89)
print("|\tMATERIAL C\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Requerimiento material |\t{TRGMCS1}\t|\t{TRGMCS2}\t|{TRGMC21}\t|")
print("-"*89)
print(f"|( + ) Inventario Final |\t{IFMCS1}\t\t|\t{IFMCS2}\t\t|\t{IFMC21}\t|")
print("-"*89)
print(f"|Total de Materiales    |\t{TTMCS1}\t|\t{TTMCS2}\t|\t{TTMC21}|")
print("-"*89)
print(f"|( + ) Inventario Final |\t{IIMCS1}\t\t|\t{IIMCS2}\t\t|\t{IIMC21}\t|")
print("-"*89)
print(f"|Material a comprar     |\t{MCMCS1}\t|\t{MCMCS2}\t|\t{MCMC21}|")
print("-"*89)
print(f"|Precio de Compra       |\t{PCMCS1}\t\t|\t{PCMCS2}\t\t|\t  \t|")
print("-"*89)
print(f"|Total MaterialC en $   |\t{TMCPS1}\t|\t{TMCPS2}\t|\t{TMCP21}|")
print("-"*89)
print(f"|Compras totales        |\t{CTS1}\t|\t{CTS2}\t|\t{CT21}|")
print("-"*89)


#--------------------------------------------------------------------------------------------
#6. Determinación del saldo de Proveedores y Flujo de Salidas

TP21=SPT20+CT21
SPT21=CT21/2
TSD21=SPT20+SPT21
TSP2021=TP21-TSD21

print("\n")
print("-"*73)
print("|6. Determinación del saldo de Proveedores y Flujo de Salidas\t\t|")
print("-"*73)
print("|\tDescripción \t|\t Importe \t|\t Total \t\t|")
print("-"*73)
print(f"|SaldoProveedor 31/12/20|\t\t \t|\t{SPT20}\t\t|")
print("-"*73)
print(f"|Compras 2021: \t\t|\t\t\t|\t{CT21}\t|")
print("-"*73)
print(f"|Total de Proveedor 2021|\t\t\t|\t{TP21}\t|")
print("-"*73)
print(f"|Salidas de Efectivo:   |\t\t \t|\t\t \t|")
print("-"*73)
print(f"|Por Proveedor  del 2020|\t{SPT20}\t\t|\t\t \t|")
print("-"*73)
print(f"|Por Proveedor  del 2021|\t{SPT21}\t|\t\t \t|")
print("-"*73)
print(f"|Total de Salidas 2021: |\t{TSD21}\t|\t{TSD21}\t|")
print("-"*73)
print(f"|SaldoProveedores 2021: |\t\t \t|\t{TSP2021}\t|")
print("-"*73)
#--------------------------------------------------------------------------------------------
#7. Presupuesto de Mano de Obra Directa
while(True):
    try:
        print("\n7. Presupuesto de Mano de Obra Directa.")
        print("PRODUCTO 1")
        #PRODUCTO 1
        #Primer semestre
        HRUP1S1=float(input("Ingrese las horas requeridas por unidad del producto 1 semestre 1: "))
        THRP1S1= HRUP1S1 * UniProducirS1P1

        CHP1S1=float(input("Ingrese la cuota por hora del producto 1 semestre 1: "))
        IMODP1S1= THRP1S1 * CHP1S1

        #Segundo semestre
        HRUP1S2=float(input("Ingrese las horas requeridas por unidad del producto 1 semestre 2: "))
        THRP1S2= HRUP1S2 * UniProducirS2P1

        CHP1S2=float(input("Ingrese la cuota por hora del producto 1 semestre 2: "))
        IMODP1S2= THRP1S2 * CHP1S2

        #Anual
        HRUP1A=float(input("Ingrese las horas requeridas por unidad del producto 1 anual: "))
        THRP1A= HRUP1A * T2021UniProdP1

        CHP1A= CHP1S1 + CHP1S2
        IMODP1A= IMODP1S1 +  IMODP1S2

        print("PRODUCTO 2")
        #Primer semestre
        HRUP2S1=float(input("Ingrese las horas requeridas por unidad del producto 2 semestre 1: "))
        THRP2S1= HRUP2S1 * UniProducirS1P2

        CHP2S1=float(input("Ingrese la cuota por hora del producto 2 semestre 1: "))
        IMODP2S1= THRP2S1 * CHP2S1

        #Segundo semestre
        HRUP2S2=float(input("Ingrese las horas requeridas por unidad del producto 2 semestre 2: "))
        THRP2S2= HRUP2S2 * UniProducirS2P2

        CHP2S2=float(input("Ingrese la cuota por hora del producto 2 semestre 2: "))
        IMODP2S2= THRP2S2 * CHP2S2

        #Anual
        HRUP2A=float(input("Ingrese las horas requeridas por unidad del producto 2 anual: "))
        THRP2A= HRUP2A * T2021UniProdP2

        CHP2A= CHP2S1 + CHP2S2
        IMODP2A= IMODP2S1 + IMODP2S2

        print("PRODUCTO 3")
        #Primer semestre
        HRUP3S1=float(input("Ingrese las horas requeridas por unidad del producto 3 semestre 1: "))
        THRP3S1= HRUP3S1 * UniProducirS1P3

        CHP3S1=float(input("Ingrese la cuota por hora del producto 3 semestre 1: "))
        IMODP3S1= THRP3S1 * CHP3S1

        #Segundo semestre
        HRUP3S2=float(input("Ingrese las horas requeridas por unidad del producto 3 semestre 2: "))
        THRP3S2= HRUP3S2 * UniProducirS2P3

        CHP3S2=float(input("Ingrese la cuota por hora del producto 3 semestre 2: "))
        IMODP3S2= THRP3S2 * CHP3S2

        #Anual
        HRUP3A=float(input("Ingrese las horas requeridas por unidad del producto 3 anual: "))
        THRP3A= HRUP3A * T2021UniProdP3
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
CHP3A= CHP3S1 + CHP3S2
IMODP3A= IMODP3S1 + IMODP3S2

#TOTAL DE HORAS
#Primer semestre
THRPS1= THRP1S1 + THRP2S1 + THRP3S1

#Segundo semetre
THRPS2= THRP1S2 + THRP2S2 + THRP3S2

#Anual
THRA= THRP1A + THRP2A + THRP3A

#TOTAL M.O.D
#Primer semestre
TMODPS1= IMODP1S1 + IMODP2S1 + IMODP3S1

#Segundo semetre
TMODPS2= IMODP1S2 + IMODP2S2 + IMODP3S2

#Anual
TMODA= IMODP1A + IMODP2A + IMODP3A
print("\n")
print("-"*89)
print("|7. Presupuesto de Mano de Obra Directa\t\t\t\t\t\t\t|\t")
print("-"*89)
print("|\tPRODUCTOS \t|\t1er Semestre\t|\t 2do Semestre \t|\t 2021\t|")
print("-"*89)
print("|\tPRODUCTO MC\t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a producir:   |\t{UniProducirS1P1}\t\t|\t{UniProducirS2P1}\t\t|\t{T2021UniProdP1}\t|")
print("-"*89)
print(f"| Horas req x unidad:   |\t{HRUP1S1}\t\t|\t{HRUP1S2}\t\t|\t{HRUP1A}\t|")
print("-"*89)
print(f"|Total de horas:        |\t{THRP1S1}\t\t|\t{THRP1S2}\t\t|\t{THRP1A}\t|")
print("-"*89)
print(f"| Cuota por hora:       |\t{CHP1S1}\t\t|\t{CHP1S2}\t\t|\t{CHP1A}\t|")
print("-"*89)
print(f"| Importe de M.O.D $:   |\t{IMODP1S1}\t|\t{IMODP1S2}\t|\t{IMODP1A}|")
print("-"*89)
print("|\tPRODUCTO MS \t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a producir    |\t{UniProducirS1P2}\t\t|\t{UniProducirS2P2}\t\t|\t{T2021UniProdP2}\t|")
print("-"*89)
print(f"| Horas req x unidad    |\t{HRUP2S1}\t\t|\t{HRUP2S2}\t\t|\t{HRUP2A}\t|")
print("-"*89)
print(f"|Total de horas req     |\t{THRP2S1}\t\t|\t{THRP2S2}\t\t|\t{THRP2A}\t|")
print("-"*89)
print(f"| Cuota por hora        |\t{CHP2S1}\t\t|\t{CHP2S2}\t\t|\t{CHP2A}\t|")
print("-"*89)
print(f"| Importe de M.O.D $    |\t{IMODP2S1}\t|\t{IMODP2S2}\t|\t{IMODP2A}|")
print("-"*89)
print("|\tPRODUCTO MR \t|\t \t   \t|\t \t   \t|\t  \t|")
print("-"*89)
print(f"|Unidades a producir    |\t{UniProducirS1P3}\t\t|\t{UniProducirS2P3}\t\t|\t{T2021UniProdP3}\t|")
print("-"*89)
print(f"| Horas req x unidad    |\t{HRUP3S1}\t\t|\t{HRUP3S2}\t\t|\t{HRUP3A}\t|")
print("-"*89)
print(f"|Total de horas req     |\t{THRP3S1}\t\t|\t{THRP3S2}\t\t|\t{THRP3A}\t|")
print("-"*89)
print(f"| Cuota por hora        |\t{CHP3S1}\t\t|\t{CHP3S2}\t\t|\t{CHP3A}\t|")
print("-"*89)
print(f"|Importe de M.O.D $     |\t{IMODP3S1}\t|\t{IMODP3S2}\t|\t{IMODP3A}|")
print("-"*89)
print(f"|Totalhoras reqxsem $   |\t{THRPS1}\t\t|\t{THRPS2}\t\t|\t{THRA}|")
print("-"*89)
print(f"|Total M.O.D xsem $     |\t{TMODPS1}\t|\t{TMODPS2}\t|\t{TMODA}|")
print("-"*89)
#--------------------------------------------------------------------------------------------
#8. Presupuesto de Gastos Indirectos de Fabricación

while(True):
    try:
        print("\n8. Presupuesto de Gastos Indirectos de Fabricación.")
        #Primer semestre
        DS1=int(input("Ingrese la depreciacion del 1er semestre: "))
        SS1=int(input("Ingrese el saldo de seguros del 1er semestre: "))
        SMS1=int(input("Ingrese el saldo de mantenimiento del 1er semestre: "))
        ES1=int(input("Ingrese los energeticos del 1er semestre: "))
        VS1=int(input("Ingrese los varios del 1er semestre: "))
        TGIFS1= DS1 + SS1 + SMS1 + ES1 + VS1

        #Segundo semestre
        DS2=int(input("Ingrese la depreciacion del 1er semestre: "))
        SS2=int(input("Ingrese el saldo de seguros del 1er semestre: "))
        SMS2=int(input("Ingrese el saldo de mantenimiento del 1er semestre: "))
        ES2=int(input("Ingrese los energeticos del 1er semestre: "))
        VS2=int(input("Ingrese los varios del 1er semestre: "))
        TGIFS2= DS2 + SS2 + SMS2 + ES2 + VS2
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
#Anual
DA= DS1 + DS2
SA= SS1 + SS2
SMA= SMS1 + SMS2
EA= ES1 + ES2
VA= VS1 + VS2 
TGIFA= DA + SA + SMA + EA + VA

#COSTO POR HORA DE G.I.F
CDCHGIF= TGIFA / THRA

print("\n")
print("-"*89)
print("|8. Presupuesto de Gastos Indirectos de Fabricación\t\t\t\t\t|")
print("-"*89)
print(f"|\t\tDepreciacion              |\t{DS1}\t|\t{DS2}\t|\t{DA}\t|")
print("-"*89)
print(f"|\t\tSeguros                   |\t{SS1}\t|\t{SS2}\t|\t{SA}\t|")
print("-"*89)
print(f"|\t\tMantenimiento             |\t{SMS1}\t|\t{SMS2}\t|\t{SMA}\t|")
print("-"*89)
print(f"|\t\tEnergeticos               |\t{ES1}\t|\t{ES2}\t|\t{EA}\t|")
print("-"*89)
print(f"|\t\tVarios                    |\t{VS1}\t|\t{VS2}\t|\t{VA}\t|")
print("-"*89)
print(f"|\t\tTotal G.I.F x sem:$       |\t{TGIFS1}\t|\t{TGIFS2}\t|\t{TGIFA}\t|")
print("-"*89)
print(f"|Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion\t|")
print("-"*89)
print(f"|\tTotal de G.I.F                    |\t\t\t\t|\t{TGIFA}\t|")
print("-"*89)
print(f"|\t(/)Total de horas M.O.D Anual     |\t\t\t\t|\t{THRA}|")
print("-"*89)
print(f"|\t(=)Costo por hora de G.I.F        |\t\t\t\t|{CDCHGIF}|")
print("-"*89)
#-------------------------------------------------------------------------------------------
#9. Presupuesto de Gastos de Operación
while(True):
    try:
        print("\n9. Presupuesto de Gastos de Operación.")
        #Primer semestre
        DS1=int(input("Ingrese la depreciacion del 1er semestre: "))
        SYSS1=int(input("Ingrese los sueldos y salarios del 1er semestre: "))
        CS1= TVS1 * .01
        VS1=int(input("Ingrese los varios del 1er semestre: "))
        IPS1=int(input("Ingrese el Interes del Prestamo del 1er semestre: "))
        TGOPS1= DS1 + SYSS1 + CS1 + VS1 + IPS1

        #Segundo semestre
        DS2=int(input("Ingrese la depreciacion del 2do semestre: "))
        SYSS2=int(input("Ingrese los sueldos y salarios del 2do semestre: "))
        CS2= TVS2 * .01
        VS2=int(input("Ingrese los varios del 2do semestre: "))
        IPS2=int(input("Ingrese el Interes del Prestamo del 2do semestre: "))
        TGOPS2= DS2 + SYSS2 + CS2 + VS2 + IPS2
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
#Anual
DAA= DS1 + DS2
SYSA= SYSS1 + SYSS2
CA= CS1 + CS2
VAA= VS1 + VS2
IPA= IPS1 + IPS2
TGOPA= DAA + SYSA + CA + VAA + IPA

print("\n")
print("-"*89)
print("|9. Presupuesto de Gastos de Operación\t\t\t\t\t\t\t|")
print("-"*89)
print(f"|Depreciacion:  |\t{DS1}\t\t|\t{DS2}\t\t|\t{DAA}\t\t|")
print("-"*89)
print(f"|SueldoSalario: |\t{SYSS1}\t\t|\t{SYSS2}\t\t|\t{SYSA}\t\t|")
print("-"*89)
print(f"|Comisiones:    |\t{CS1}\t|\t{CS2}\t|\t{CA}\t|")
print("-"*89)
print(f"|Varios:        |\t{VS1}\t\t|\t{VS2}\t\t|\t{VAA}\t\t|")
print("-"*89)
print(f"|Interesespres: |\t{IPS1}\t\t|\t{IPS2}\t\t|\t{IPA}\t\t|")
print("-"*89)
print(f"|Total GastosO$:|\t{TGOPS1}\t|\t{TGOPS2}\t|\t{TGOPA}\t|")
print("-"*89)


#--------------------------------------------------------------------------------------------

#10. Determinacion del costo unitario de productos terminados
while(True):
    try:
        print("\n10. Determinacion del costo unitario de productos terminados.")
        #Producto 1
        CantidadMA1=float(input("Ingrese la cantidad del material A para producto 1: "))
        CUA1= PCMAS2 * CantidadMA1
        CantidadMB1=float(input("Ingrese la cantidad del material B para producto 1: "))
        CUB1= PCMBS2 * CantidadMB1
        CantidadMC1=float(input("Ingrese la cantidad del material C para producto 1: "))
        CUC1= PCMCS2 * CantidadMC1
        CUMo1= CHP1S2 * HRUP1S2
        CUG1= CDCHGIF * HRUP1S2
        CU1= CUA1 + CUB1 + CUC1 + CUMo1 + CUG1

        #Producto 2
        CantidadMA2=float(input("Ingrese la cantidad del material A para producto 2: "))
        CUA2= PCMAS2 * CantidadMA2
        CantidadMB2=float(input("Ingrese la cantidad del material B para producto 2: "))
        CUB2= PCMBS2 * CantidadMB2
        CantidadMC2=float(input("Ingrese la cantidad del material C para producto 2: "))
        CUC2= PCMCS2 * CantidadMC2
        CantidadMO2=float(input("Ingrese la cantidad de la mano de obra: "))
        CUMo2= CHP2S2 * CantidadMO2
        CantidadGIF2=float(input("Ingrese la cantidad de gastos indirectos de fabricacion: "))
        CUG2= CDCHGIF * CantidadGIF2
        CU2= CUA2 + CUB2 + CUC2 + CUMo2 + CUG2

        #Producto 3
        CantidadMA3=float(input("Ingrese la cantidad del material A para producto 3: "))
        CUA3= PCMAS2 * CantidadMA3
        CantidadMB3=float(input("Ingrese la cantidad del material B para producto 3: "))
        CUB3= PCMBS2 * CantidadMB3
        CantidadMC3=float(input("Ingrese la cantidad del material C para producto 3: "))
        CUC3= PCMCS2 * CantidadMC3
        CUMo3= CHP1S2 * HRUP3S2
        CantidadGIF3=float(input("Ingrese la cantidad de gastos indirectos de fabricacion: "))
        CUG3= CDCHGIF * CantidadGIF3
        CU3= CUA3 + CUB3 + CUC3 + CUMo3 + CUG3
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
print("\n")
print("-"*89)
print("|10. Determinación del Costo Unitario de Productos Terminados\t\t\t\t|")
print("-"*89)
print("|\tDESCRIPCION \t|\tCosto\t|\t Cantidad \t|\t Costo Unitario\t|")
print("-"*89)
print("|\tPRODUCTO CL\t|\t    \t|\t \t   \t|\t\t  \t|")#############
print("-"*89)
print(f"|\tMaterial A\t|\t{PCMAS2}\t|\t{CantidadMA1}\t\t|{CUA1}\t|")
print("-"*89)
print(f"|\tMaterial B\t|\t{PCMBS2}\t|\t{CantidadMB1}\t\t|\t{CUB1}\t\t|")
print("-"*89)
print(f"|\tMaterial C\t|\t{PCMCS2}\t|\t{CantidadMC1}\t\t|\t{CUC1}\t\t|")
print("-"*89)
print(f"|\tMano de Obra\t|\t{CHP1S2}\t|\t{HRUP1S2}\t\t|\t{CUMo1}\t\t|")
print("-"*89)
print(f"|\tGastosIndiFab\t|{CDCHGIF}|\t{HRUP1S2}\t\t|{CUG1}\t|")
print("-"*89)
print(f"|\tCOSTO UNITARIO\t|\t    \t|\t\t \t|{CU1}\t|")
print("-"*89)
print("|\tPRODUCTO CE\t|\t   \t|\t \t   \t|\t\t  \t|")########
print("-"*89)
print(f"|\tMaterial A\t|\t{PCMAS2}\t|\t{CantidadMA2}\t\t|{CUA2}\t|")
print("-"*89)
print(f"|\tMaterial B\t|\t{PCMBS2}\t|\t{CantidadMB2}\t\t|\t{CUB2}\t\t|")
print("-"*89)
print(f"|\tMaterial C\t|\t{PCMCS2}\t|\t{CantidadMC2}\t\t|\t{CUC2}\t\t|")
print("-"*89)
print(f"|\tMano de Obra\t|\t{CHP2S2}\t|\t{CantidadMO2}\t\t|\t{CUMo2}\t\t|")
print("-"*89)
print(f"|\tGastosIndiFab\t|{CDCHGIF}|\t{CantidadGIF2}\t\t|{CUG2}\t|")
print("-"*89)
print(f"|\tCOSTO UNITARIO\t|\t    \t|\t\t \t|{CU2}\t|")
print("-"*89)
print("|\tPRODUCTO CR\t|\t   \t|\t \t   \t|\t\t  \t|")#######
print("-"*89)
print(f"|\tMaterial A\t|\t{PCMAS2}\t|\t{CantidadMA3}\t\t|\t\t{CUA3}\t|")
print("-"*89)
print(f"|\tMaterial B\t|\t{PCMBS2}\t|\t{CantidadMB3}\t\t|\t{CUB3}\t\t|")
print("-"*89)
print(f"|\tMaterial C\t|\t{PCMCS2}\t|\t{CantidadMC3}\t\t|\t{CUC3}\t\t|")
print("-"*89)
print(f"|\tMano de Obra\t|\t{CHP1S2}\t|\t{HRUP3S2}\t\t|\t{CUMo3}\t\t|")
print("-"*89)
print(f"|\tGastosIndiFab\t|{CDCHGIF}|\t{CantidadGIF3}\t\t|{CUG3}|")
print("-"*89)
print(f"|\tCOSTO UNITARIO\t|\t    \t|\t\t \t|{CU3}\t|")
print("-"*89)


#--------------------------------------------------------------------------------------------

#11. Valuacion de inventarios finales

print("\n11. Valuacion de inventarios finales.")
#Inventario final de materiales
CTMA= IFMAS2 * PCMAS2 #costo de materiales A
CTMB= IFMBS2 * PCMBS2 #costo de materiales B
CTMC= IFMCS2 * PCMCS2 #costo de materiales B
IFM= CTMA + CTMB + CTMC #inventario final de materiales

CTPT1= InvFinalS2P1 * CU1 #costo total del producto 1
CTPT2= InvFinalS2P2 * CU2 #costo total del producto 2
CTPT3= InvFinalS2P3 * CU3 #costo total del producto 3
IFPT= CTPT1 + CTPT2 + CTPT3 #inventario final de productos terminados

print("\n")
print("-"*89)
print("|11. Valuación de Inventarios Finales\t\t\t\t\t\t\t|")
print("-"*89)
print("|\t\t\t\tINVENTARIO FINAL DE MATERIALES\t\t\t\t|")#############
print("-"*89)
print("|\tDESCRIPCION \t|\tCosto\t|\t Cantidad \t|\t Costo Unitario\t|")
print("-"*89)
print(f"|\tMaterial A\t|\t{IFMAS2}\t|\t{PCMAS2}\t\t|\t\t{CTMA}\t|")
print("-"*89)
print(f"|\tMaterial B\t|\t{IFMBS2}\t|\t{PCMBS2}\t\t|\t\t{CTMB}\t|")
print("-"*89)
print(f"|\tMaterial C\t|\t{IFMCS2}\t|\t{PCMCS2}\t\t|\t\t{CTMC}\t|")
print("-"*89)
print(f"|\tInventarioFM\t|\t  \t|\t  \t\t|\t\t{IFM}\t|")
print("-"*89)###############
print("|\t\t\tINVENTARIO FINAL DE PRODUCTO TERMINADO\t\t\t\t|")#############
print("-"*89)
print("|\tDESCRIPCION \t|\tCosto\t|\t Cantidad \t|\t Costo Unitario\t|")
print("-"*89)
print(f"|\tProducto CL\t|\t{InvFinalS2P1}\t| {CU1}|\t{CTPT1}|")
print("-"*89)
print(f"|\tProducto CE\t|\t{InvFinalS2P2}\t| {CU2}|\t{CTPT2}|")
print("-"*89)
print(f"|\tProducto CR\t|\t{InvFinalS2P3}\t| {CU3}|\t{CTPT3}|")
print("-"*89)
print(f"|\tInventarioFPT\t|\t  \t|\t  \t\t|\t{IFPT}|")
print("-"*89)

#--------------------------------------------------------------------------------------------
#II. Presupuesto Financiero
while(True):
    try:
        print("\nII. Presupuesto Financiero.")
        SIM=float(input("Ingrese el saldo inicial de materiales: "))
        MDisp= SIM + CT21 #materiales disponibles
        MUtil= MDisp - IFM #materiales utilizados
        CdP= MUtil + TMODA + TGIFA #costo de produccion
        INPT=float(input("Ingrese el inventario inicial de productos terminados: "))
        TPD= CdP + INPT #total de materiales disponibles
        CV= TPD - IFPT #costo de ventas
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")

print("-"*89)
print("|Madererias Mexicanas S.A de C.V\t\t\t\t\t\t\t|")
print("-"*89)
print("| Estado de Costo de Producción y Ventas  (Presupuesto del 1/Enero al 31/Diciembre/2021)|")
print("-"*89)
print(f"|\tSaldo Inicial de materiales\t|\t  \t|\t  \t|\t{SIM}\t|")
print("-"*89)
print(f"|\tCompras de materiales\t        |\t  \t|\t  \t|{CT21}\t|")
print("-"*89)
print(f"|\tMaterial disponible\t        |\t  \t|\t  \t|\t{MDisp}|")
print("-"*89)
print(f"|\tInventarioFinal de Materiales\t|\t  \t|\t  \t|\t{IFM}\t|")
print("-"*89)
print(f"|\tMateriales Utilizados\t        |\t  \t|\t  \t|{MUtil}\t|")
print("-"*89)
print(f"|\tMano de Obra Directa\t        |\t  \t|\t  \t|\t{TMODA}|")
print("-"*89)
print(f"|\tGastosFabricaciónIndirectos\t|\t  \t|\t  \t|\t{TGIFA}|")
print("-"*89)
print(f"|\tCosto de Producción\t        |\t  \t|\t  \t|\t{CdP}|")
print("-"*89)
print(f"|\tInventarioInicial PT\t        |\t  \t|\t  \t|\t{INPT}|")
print("-"*89)
print(f"|\tTotal Producción Disponible\t|\t  \t|\t  \t|\t{TPD}|")
print("-"*89)
print(f"|\tInventarioFinal PT\t        |\t  \t|\t  \t|{IFPT}|")
print("-"*89)
print(f"|\tCosto de Ventas\t                |\t  \t|\t  \t|{CV}|")
print("-"*89)

#--------------------------------------------------------------------------------------------

print("\nII. Estado de resultados.")
UB= TVA - CV #utilidad bruta
UO= UB - TGOPA #utilidad de operacion
ISR= UO * 0.3 #ISR
PTU= UO * 0.1 #PTU
UNeta= UO - ISR - PTU #Utilidad neta

print("\n")
print("-"*89)
print("|Madererias Mexicanas S.A de C.V\t\t\t\t\t\t\t|")
print("-"*89)
print("|Estado de Resultados (Presupuesto del 1/Enero al 31/Diciembre/2021)\t\t\t|")
print("-"*89)
print(f"|\tVentas\t\t|\t  \t|\t  \t|\t{TVA}\t\t|")#Cambie la variable 
print("-"*89)
print(f"|\tCostos ventas\t|\t  \t|\t  \t|\t{CV}\t|")
print("-"*89)
print(f"|\tUtilidad bruta\t|\t  \t|\t  \t|\t{UB}\t|")
print("-"*89)
print(f"|\tGastosOp\t |\t  \t|\t  \t|\t{TGOPA}\t\t|")
print("-"*89)
print(f"|\tUtilOp\t       |\t  \t|\t  \t|\t{UO}\t|")
print("-"*89)
print(f"|\tISR\t        |\t  \t|\t  \t|\t{ISR}\t|")
print("-"*89)
print(f"|\tPTU\t        |\t  \t|\t  \t|\t{PTU}\t|")
print("-"*89)
print(f"|\tUtilidad Neta\t|\t  \t|\t  \t|\t{UNeta}\t|")
print("-"*89)

#--------------------------------------------------------------------------------------------
while(True):
    try:
        print("\nII. Estado de Flujo de Efectivo.")
        SaldoIniEfectivo=int(input("Ingrese el Saldo Inicial de Efectivo:"))
        CAFMAQ=int(input("Ingrese la compra de activo fijo(maquinaria):"))
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")

TotalEntradas=Cobranza2021+SaldoClientes
EfectivoDisp=SaldoIniEfectivo+TotalEntradas
PGIF=TGIFA-DA
PGOP=TGOPA-DAA
TSalidas=SPT21+SPT20+TMODA+PGIF+PGOP+CAFMAQ+ISR2020+ISR2021 #Creo que al ultimo ISR se le agrega el "2021" ya lo declare arriba 
FluEfectActual1=EfectivoDisp-TSalidas

print("\n")
print("-"*89)
print("|Madererias Mexicanas S.A de C.V\t\t\t\t\t\t\t|")
print("-"*89)
print("|Estado de Flujo de Efectivo (Presupuesto del 1/Enero al 31/Diciembre/2021)\t\t|")
print("-"*89)
print(f"|\t Saldo Inicial de Efectivo \t|\t  \t|\t{FluEfectActual}\t|")
print("-"*89)
print("|\t Entradas: \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Cobranza 2021 \t|\t {Cobranza2021} \t|\t   \t|")
print("-"*89)
print(f"|\t Cobranza 2020 \t|\t {SaldoClientes} \t|\t   \t|")
print("-"*89)
print(f"|\t Total de Entradas \t|\t  \t|\t {TotalEntradas} \t|")
print("-"*89)
print(f"|\t Efectivo Disponible \t|\t  \t|\t {EfectivoDisp} \t|")
print("-"*89)
print("|\t Salidas: \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Proveedores 2021 \t|\t {SPT21} \t|\t   \t|")
print("-"*89)
print(f"|\t Proveedores 2020 \t|\t {SPT20} \t|\t   \t|")
print("-"*89)
print(f"|\t Pago Mano de Obra Directa \t|\t {TMODA} \t|\t   \t|")
print("-"*89)
print(f"|\t Pago Gastos Indirectos de Fabricación \t|\t {PGIF} \t|\t   \t|")
print("-"*89)
print(f"|\t Pago de Gastos de Operación \t|\t {PGOP} \t|\t   \t|")
print("-"*89)
print(f"|\t Compra de Activo Fijo (Maquinaria) \t|\t {CAFMAQ} \t|\t   \t|")
print("-"*89)
print(f"|\t Pago ISR 2020 \t|\t {ISR2020} \t|\t   \t|")
print("-"*89)
print(f"|\t Pago ISR 2021 \t|\t {ISR2021} \t|\t   \t|")
print("-"*89)
print(f"|\t Total de Salidas \t|\t  \t|\t {TSalidas} \t|")
print("-"*89)
print(f"|\t Flujo de Efectivo Actual \t|\t  \t|\t {FluEfectActual1} \t|")
print("-"*89)


#--------------------------------------------------------------------------------------------
while(True):
    try:
        print("\nII. Balance General.")
        DD=int(input("Ingrese la cantidad de Deudores Diversos:"))
        FM=int(input("Ingrese la cantidad de Funcionarios y empleados:"))

        TAC = FluEfectActual1 + STClientes2021 +  DD + IFM + FM + IFPT

        MT=int(input("Ingrese el Monto del Terreno:"))

        BPYE1= BPYE + CAFMAQ
        DAC1= DAC - DA - DAA
        TANC= MT + BPYE1 + DAC1
        AT= TAC + TANC

        DP=int(input("Ingrese la cantidad de Documentos por Pagar:"))

        TPCP= TSP2021 + DP + ISR + PTU

        PB=int(input("Ingrese la cantidad de Prestamos Bancarios:"))

        TPLP= PB
        PT= TPCP + TPLP 

        CA=int(input("Ingrese la cantidad del Capital Aportado:"))
        CG=int(input("Ingrese la cantidad del Capital Ganado:"))

        TCC= CA + CG + UNeta
        SPC= PT + TCC
        break
    except:
        print("\n****************OPCION ERRONEA, INTENTE OTRA VEZ****************")
        print("\n")
print("\n")
print("-"*89)
print("|Madererias Mexicanas S.A de C.V\t\t\t\t\t\t\t|")
print("-"*89)
print("|Balance General (Presupuesto del 1/Enero al 31/Diciembre/2021)\t\t\t\t|")
print("-"*89)
print("|\t ACTIVO  \t|\t  \t|\t   \t|")
print("-"*89)
print("|\t Circulante  \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Efectivo \t|\t {FluEfectActual1} \t|\t   \t|")
print("-"*89)
print(f"|\t Clientes \t|\t {STClientes2021} \t|\t   \t|")
print("-"*89)
print(f"|\t Deudores Diversos \t|\t {DD} \t|\t  \t|")
print("-"*89)
print(f"|\t Inventario Materiales \t|\t {IFM} \t|\t  \t|")
print("-"*89)
print(f"|\t Funcionarios Empleados \t|\t {FM} \t|\t  \t|")
print("-"*89)
print(f"|\t Inventario Pod Terminado \t|\t {IFPT} \t|\t  \t|")
print("-"*89)
print(f"|\t Total Activo Circulantes: $ \t|\t  \t|\t {TAC} \t|")
print("-"*89)
print("|\t No Circulante  \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Terreno \t|\t {MT} \t|\t  \t|")
print("-"*89)
print(f"|\t Planta Equipo \t|\t {BPYE1} \t|\t  \t|")
print("-"*89)
print(f"|\t Depreciacion Acum \t|\t {DAC1} \t|\t  \t|")
print("-"*89)
print(f"|\t Total Activo No Circulantes: $ \t|\t  \t|\t {TANC} \t|")
print("-"*89)
print(f"|\t ACTIVO TOTAL: $ \t|\t  \t|\t {AT} \t|")
print("-"*89)
print("|\t PASIVO  \t|\t  \t|\t   \t|")
print("-"*89)
print("|\t Corto Plazo  \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Proveedores \t|\t {TSP2021} \t|\t  \t|")
print("-"*89)
print(f"|\t Doc x Pagar \t|\t {DP} \t|\t  \t|")
print("-"*89)
print(f"|\t ISR x Pagar \t|\t {ISR} \t|\t  \t|")
print("-"*89)
print(f"|\t PTU x Pagar \t|\t {PTU} \t|\t  \t|")
print("-"*89)
print(f"|\t Total Pasivo CP: $ \t|\t  \t|\t {TPCP} \t|")
print("-"*89)
print("|\t Largo Plazo  \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Prestamos Bancarios \t|\t {PB} \t|\t  \t|")
print("-"*89)
print(f"|\t Total Pasivo LP: $ \t|\t  \t|\t {TPLP } \t|")
print("-"*89)
print(f"|\t PASIVO TOTAL: $ \t|\t  \t|\t {PT} \t|")
print("-"*89)
print("|\t CAPITAL CONTABLE  \t|\t  \t|\t   \t|")
print("-"*89)
print(f"|\t Capital Aportado \t|\t {CA} \t|\t  \t|")
print("-"*89)
print(f"|\t Capital Ganado \t|\t {CG} \t|\t  \t|")
print("-"*89)
print(f"|\t Utilidad Ejercicio \t|\t {UNeta} \t|\t  \t|")
print("-"*89)
print(f"|\t Total Capital Contable: $ \t|\t  \t|\t {TCC} \t|")
print("-"*89)
print(f"|\t SUMA PASIVO Y CAPITAL: $ \t|\t  \t|\t {SPC} \t|")
print("-"*89)


