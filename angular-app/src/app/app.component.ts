import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import * as _ from 'lodash';
import moment from 'moment';
import { v4 as uuidv4 } from 'uuid';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'angular-app';
  currentDate = moment().format('MMMM Do YYYY');
  uniqueId = uuidv4();
  items = _.uniq([1, 2, 2, 3, 3, 4]);
}
