import { Component, OnInit } from '@angular/core';
import {submissionInterests} from './submissionInterests'

import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-interests-page',
  templateUrl: './interests-page.component.html',
  styleUrls: ['./interests-page.component.css']
})
export class InterestsPageComponent implements OnInit {

	latitude = 51.5033640;
	longitude = -0.1276250;

	fs: string = '{"data": [{"activity": "Jazz Club", "lat": 37.77635001768186, "lng": -122.42153942584991, "name": "SFJazz Center", "contact": "(866) 920-5299", "like": 389, "location": "201 Franklin St (at Fell St) San Francisco, CA 94102 United States"}, {"activity": "Mini Golf", "lat": 37.805965, "lng": -122.42273, "like": 1, "name": "Subpar Miniature Golf", "contact": null, "location": "San Francisco, CA 94109 United States"}, {"activity": "BBQ Joint", "lat": 37.77612534143469, "lng": -122.43814234566274, "like": 801, "name": "4505 Burgers & BBQ", "contact": "(415) 231-6993", "location": "705 Divisadero St (at Grove St) San Francisco, CA 94117 United States"}, {"activity": "Bubble Tea Shop", "lat": 37.75398223901287, "lng": -122.490292773866, "like": 13, "name": "Bubble Tea & Dessert Cafe", "contact": "(415) 662-8233", "location": "1788 32nd Ave San Francisco, CA 94122 United States"}]}';
	
	arr = new Array<boolean>(50).fill(false);
	arr2 = new Array<boolean>(50).fill(false);

	isLinear = false;
	firstFormGroup: FormGroup;
	secondFormGroup: FormGroup;


	interests: string[] = ["Aquarium", "Arcade", "Art Gallery", "Bowling Alley", "Casino", "Circus", "Comedy Club", "Concert Hall", "Go Kart Track", "Historic Site", "Karaoke Box", "Laser Tag", "Mini Golf", "Movie Theater", "Museum", "Jazz Club", "Opera House", "Theme Park", "Zoo", "Nightclub", "Lounge", "Gym / Fitness Center", "Beach", "Hot Spring", "Lake", "Lighthouse", "Mountain", "National Park", "Nature Preserve", "Park", "Rock Climbing Spot", "Trail", "Vineyard", "Waterfront", "Capitol Building", "Bookstore", "Candy Store", "Chocolate Shop", "Clothing Store", "Comic Shop", "Farmers Market", "Gaming Cafe", "Massage Studio", "Winery", "Volcano", "Bay", "Athletics & Sports"];

	foods: string[] = ["Afghan Restaurant", "Ethiopian Restaurant", "American Restaurant", "Chinese Restaurant", "Filipino Restaurant", "Indonesian Restaurant", "Japanese Restaurant", "Korean Restaurant", "Mongolian Restaurant", "Australian Restaurant", "BBQ Joint", "Bubble Tea Shop", "Buffet", "Burget Joint", "Cajun / Creole Restaurant", "Caribbean Restaurant", "Coffee Shop", "Creperie", "Cupcake Shop", "Ice Cream Shop", "Donut Shop", "Falafel Restaurant", "Fast Food Restaurant", "Fish & Chips Shop", "French Restaurant", "Fried Chicken Joint", "German Restaurant", "Greek Restaurant", "Halal Restaurant", "Hawaiian Restaurant", "Indian Restaurant", "Indian Restaurant", "Mexican Restaurant", "Israeli Restaurant", "Persian Restaurant", "Lebanese Restaurant", "Pizza Place", "Russian Restaurant", "Sandwich Place", "Seafood Restaurant", "Bar"];

  constructor(private _formBuilder: FormBuilder) { }

  ngOnInit() {
  this.firstFormGroup = this._formBuilder.group({
      firstCtrl: ['', Validators.required]
    });
    this.secondFormGroup = this._formBuilder.group({
      secondCtrl: ['', Validators.required]
    });
  }

  onClick(index: number) {
  	console.log("Interest Index Clicked: " + index);
  	if(this.arr[index] === false) {
    this.arr[index] = true;
    } else {
    	this.arr[index] = false;
    }
  }

  onClick2(index: number) {
  	console.log("Food Index Clicked: " + index);
  	if(this.arr2[index] === false) {
    this.arr2[index] = true;
    } else {
    	this.arr2[index] = false;
    }
  }

  onSubmit() {
  	const interests = new submissionInterests();
  	for (let i = 0; i < this.arr.length; i++) {
        if (this.arr[i] === true) {
            interests.addInterestsNode(this.interests[i]);
            console.log("Added: " + this.interests[i]);
        }
    }
    for (let i = 0; i < this.arr2.length; i++) {
        if (this.arr2[i] === true) {
            interests.addFoodNode(this.foods[i]);
            console.log("Added: " + this.foods[i]);
        }
    }
	
	// const obj = JSON.parse(JSON.stringify(interests));
	console.log(JSON.stringify(interests));
    
  }

  goUp(index: number) {
  	const temp = this.interests[index - 1];
    this.interests[index - 1] = this.interests[index];
    this.interests[index] = temp;

  }

  goDown(index: number) {
  	const temp = this.interests
  }

}
