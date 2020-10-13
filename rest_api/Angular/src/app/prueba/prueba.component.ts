import { Component, OnInit } from '@angular/core';
import { Categoria } from '../entidades/categoria/categoria';
import { CategoriaService } from '../Servicios/categoria/categoria.service';

@Component({
  selector: 'app-prueba',
  templateUrl: './prueba.component.html',
  styleUrls: ['./prueba.component.css']
})
export class PruebaComponent implements OnInit {

   nuevaCategoria:Categoria= new Categoria();
   listadoCategoria:Categoria[];
  constructor(private servicioCategoria:CategoriaService) { }

  ngOnInit(): void {
    this.getCategoria();
  }

  // prueba()
  // {alert("nuevo nombre de la categoria:" + this.nuevaCategoria.categoria)}

  getCategoria(){
    this.servicioCategoria.getCategorias().subscribe(
      res=>{console.log(res);
        this.listadoCategoria=res;}
      
    );
  }
}
