import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { InterestsPageComponent } from './interests-page/interests-page.component';

import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatStepperModule} from '@angular/material/stepper';

import { AgmCoreModule } from '@agm/core'


import {
    MatFormFieldModule,
    MatInputModule
} from '@angular/material';


import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';


import {NgxMaterialTimepickerModule} from 'ngx-material-timepicker';


@NgModule({
  declarations: [
    AppComponent,
    InterestsPageComponent
  ],
  imports: [
    BrowserModule,
    FormsModule, 
    ReactiveFormsModule,
    MatToolbarModule,
    MatButtonModule,
    MatStepperModule,
    MatFormFieldModule,
    BrowserAnimationsModule,
    MatInputModule,
    AgmCoreModule.forRoot({
    	apiKey: 'AIzaSyBgi9H_wWs3tWUajLTMS7Sc36A_jzku0sc'
    }),
    [NgxMaterialTimepickerModule.forRoot()]
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
