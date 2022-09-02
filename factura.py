from fpdf import FPDF

pdf = FPDF('P','mm','A4')

pdf.add_page()
pdf.set_fill_color(190)

# ----------Heading-----------
pdf.set_y(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(20,8,'HOTEL YIT VIA SEVILLA MAIRENA  ****   GS HOTELES SL', align='L')

pdf.set_y(18)
pdf.set_font('Arial','',8)
pdf.cell(20,6,'hotelviasevillamairena.com',align='L')

pdf.set_y(23)
pdf.set_font('Arial','',8)
pdf.cell(20,6,'B19537687',align='L')

pdf.set_y(28)
pdf.set_font('Arial','',8)
pdf.cell(20,6,'Av. De Los Descubrimientos s/n (41927) MAIRENA DEL ALJARAFE, SEVILLA',align='L')

pdf.set_y(33)
pdf.set_font('Arial','',8)
pdf.cell(40,6,'955417954',align='L')

pdf.set_font('Arial','',8)
pdf.cell(20,6,'hotelviasevillamairena@yithoteles.com',align='L')

pdf.image('YITHOTELES-.jpg',x=160,y=10,w=35,h=35)

# ----------Datos Factura------------
pdf.set_xy(15,60)
pdf.set_font('Arial','B',9)
pdf.cell(65,6,'DATOS FACTURA',border=True,align='C',fill=True)

pdf.ln()
pdf.set_x(15)
pdf.set_font('Arial','B',8)
pdf.cell(25,5,'NÚMERO',border='L',align='R')
pdf.set_font('Arial','',8)
pdf.cell(40,5,'MAFAC2022 5.432',border='R',align='L')

pdf.ln()
pdf.set_x(15)
pdf.set_font('Arial','B',8)
pdf.cell(25,5,'FECHA',border='L',align='R')
pdf.set_font('Arial','',8)
pdf.cell(40,5,'15/07/2022',border='R',align='L')

pdf.ln()
pdf.set_x(15)
pdf.set_font('Arial','B',8)
pdf.cell(25,5,'F. PAGO',border='L',align='R')
pdf.set_font('Arial','',8)
pdf.cell(40,5,'TARJETA',border='R',align='L')

pdf.ln()
pdf.set_x(15)
pdf.set_font('Arial','B',8)
pdf.cell(25,5,'PÁGINA',border='L',align='R')
pdf.set_font('Arial','',8)
pdf.cell(40,5,'1',border='R',align='L')

pdf.ln()
pdf.set_x(15)
pdf.set_font('Arial','B',8)
pdf.cell(25,5,'LOCALIZADOR',border='LB',align='R')
pdf.set_font('Arial','',8)
pdf.cell(40,5,'248595362458',border='RB',align='L')

#-----------Datos Titular-----------
pdf.set_xy(95,60)
pdf.set_font('Arial','B',9)
pdf.cell(100,6,'DATOS TITULAR',border=True,align='C',fill=True)

pdf.ln()
pdf.set_x(95)
pdf.set_font('Arial','',8)
pdf.cell(100,7.5,'APELLIDO1 APELLIDO2, NOMBRE',border='LR',align='L')

pdf.ln()
pdf.set_x(95)
pdf.set_font('Arial','',8)
pdf.cell(100,7.5,'DNI',border='LR',align='L')

pdf.ln()
pdf.set_x(95)
pdf.set_font('Arial','',8)
pdf.cell(100,10,'DIRECCIÓN',border='LRB',align='L')

#------------Datos Reserva-------------
pdf.set_xy(25,100)
pdf.set_font('Arial','B',9)
pdf.cell(160,6,'DATOS RESERVA',border=True,align='C',fill=True)

pdf.ln()
pdf.set_font('Arial','',8)
pdf.set_x(25)
pdf.cell(80,5,'APELLIDO1 APELLIDO2, NOMBRE',border='L',align='L')
pdf.cell(25,5,'Documento: ',align='R')
pdf.cell(55,5,'DNI',align='L',border='R')

pdf.ln()
pdf.set_x(25)
pdf.cell(13,5,'Número: ',border='L')
pdf.cell(67,5,'90.854')
pdf.cell(25,5,'Localizador: ',align='R')
pdf.cell(55,5,'25158162542',align='L',border='R')

pdf.ln()
pdf.set_x(25)
pdf.cell(25,5,'Contrato agencia: ',border='LB')
pdf.cell(55,5,'',border='B')
pdf.cell(25,5,'Email: ',border='B',align='R')
pdf.cell(55,5,'mortiz.493214@guest.booking.com',align='L',border='RB')

#----------Parte variable---------

noches = 8

pdf.set_xy(15,130)
pdf.set_font('Arial','B',9)
pdf.cell(25,6,'Fecha',border=True,align='C',fill=True)
pdf.cell(75,6,'Concepto',border=True,align='L',fill=True)
pdf.cell(20,6,'Cantidad',border=True,align='C',fill=True)
pdf.cell(20,6,'Precio',border=True,align='C',fill=True)
pdf.cell(20,6,'IVA',border=True,align='C',fill=True)
pdf.cell(20,6,'Importe',border=True,align='C',fill=True)

for i in range(noches):
    
    pdf.ln()
    pdf.set_x(15)
    pdf.set_font('Arial','',8)
    pdf.cell(25,7,'17/05/2022',border=True,align='C')
    pdf.cell(75,7,'CARGO POR HABITACIÓN 703',border=True,align='L')
    pdf.cell(20,7,'1',border=True,align='R')
    pdf.cell(20,7,'40.09',border=True,align='R')
    pdf.cell(20,7,'10.00',border=True,align='R')
    pdf.cell(20,7,'44.10',border=True,align='R')


#--------Total factura---------
x=70
y=130+6+7*noches+10

pdf.set_xy(x,y)
pdf.set_font('Arial','B',9)
pdf.cell(50,6,'BASE IMPONIBLE',border='BTL',fill=True,align='C')
pdf.cell(25,6,'IVA',border='TB',fill=True,align='C')
pdf.cell(50,6,'TOTAL FACTURA',border='TBR',fill=True,align='C')

y=y+6
pdf.set_xy(x,y)
pdf.set_font('Arial','',8)
pdf.cell(50,5,'40.09',align='R',border='L')
pdf.cell(12,5,'10',align='C')
pdf.cell(13,5,'4.01',align='C')
pdf.set_font('Arial','B',8)
pdf.cell(50,10,'44.10',align='R',border='R')

y=y+5
pdf.set_xy(x,y)
pdf.set_font('Arial','',8)
pdf.cell(50,5,'',align='R',border='L')
pdf.cell(12,5,'21',align='C')
pdf.cell(13,5,'0.00',align='C')

y=y+5
pdf.set_xy(x,y)
pdf.cell(75,5,'Entregas a cuenta: ',align='R',border='L')
pdf.cell(50,5,'44.10',align='R',border='R')

y=y+5
pdf.set_xy(x,y)
pdf.set_font('Arial','B',8)
pdf.cell(75,5,'Total a pagar: ',align='R',border='LB')
pdf.cell(50,5,'0.00',align='R',border='RB')




pdf.output('factura.pdf','F')