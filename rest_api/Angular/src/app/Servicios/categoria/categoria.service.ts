import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Categoria } from '../../entidades/categoria/categoria';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {
 private url="http://127.0.0.1:8000/mostrarCategorias";
  constructor(private http:HttpClient) { }

  getCategorias():Observable<Categoria[]>{
    return this.http.get<Categoria[]>(this.url);

  }
}
