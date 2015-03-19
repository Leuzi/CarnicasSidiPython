# -*- coding: utf-8 -*-
'''
Created on 30/12/2011

@author: kaos
'''

class Clientes(object):
    '''
    classdocs
    '''
    #Constructo con parametros(opcionales)
    def __init__(self,idCliente=0,nombre=0,detalles=0,direccion=0,cif=0,ciudad=0,pais=0,CP=0):
        '''
        Constructor
        '''
        self.idCliente=idCliente
        self.nombre=nombre
        self.detalles=detalles
        self.direccion=direccion
        self.cif=cif
        self.ciudad=ciudad
        self.pais=pais
        self.CP=CP
        self.facturas=[]#Lista de las facturas que posee un cliente
        
    def anadirFactura(self,factura):
        #Añadimos una factura
        self.facturas.append(factura)
    
    def eliminarFactura(self,factura):
        #eliminamos una factura
        self.facturas.remove(factura)
    
    def modificarFactura(self,facturaold,facturanew):
        #modificamos una factura,
        #borramos la antigua
        self.facturas.remove(facturaold)
        #creamos la nueva
        self.facturas.append(facturanew)
   
        #obtenemos facturas
    def getFacturas(self):
        return self.facturas

    
