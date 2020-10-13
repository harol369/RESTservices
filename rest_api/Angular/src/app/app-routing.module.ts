import { Routes, RouterModule } from '@angular/router';
import { PruebaComponent } from './prueba/prueba.component'

const APP_ROUTES: Routes = [
  {path: 'categoria', component:PruebaComponent},
  {path:'**', pathMatch:'full', redirectTo:'categoria'}
];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES) 
