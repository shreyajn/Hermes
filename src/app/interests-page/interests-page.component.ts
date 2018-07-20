import { Component, OnInit } from '@angular/core';
import {submissionInterests} from './submissionInterests';
import {HttpClient} from '@angular/common/http';


import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-interests-page',
  templateUrl: './interests-page.component.html',
  styleUrls: ['./interests-page.component.css']
})
export class InterestsPageComponent implements OnInit {

	finalInterests: string[] = [];
	finalLocations: string[] = [];

	latitudes: string[] = [];
	longitudes: string[] = [];

	url: string = '';

	latitude = 37.7749;
	longitude = -122.4194;

	res: any;
	
	arr = new Array<boolean>(50).fill(false);
	arr2 = new Array<boolean>(50).fill(false);

	// finalResults = new Array<any>;

	isLinear = false;
	firstFormGroup: FormGroup;
	secondFormGroup: FormGroup;


	interests: string[] = ["Aquarium", "Arcade", "Art Gallery", "Bowling Alley", "Casino", "Circus", "Comedy Club", "Concert Hall", "Go Kart Track", "Historic Site", "Karaoke Box", "Laser Tag", "Mini Golf", "Movie Theater", "Museum", "Jazz Club", "Opera House", "Theme Park", "Zoo", "Nightclub", "Lounge", "Gym / Fitness Center", "Beach", "Hot Spring", "Lake", "Lighthouse", "Mountain", "National Park", "Nature Preserve", "Park", "Rock Climbing Spot", "Trail", "Vineyard", "Waterfront", "Capitol Building", "Bookstore", "Candy Store", "Chocolate Shop", "Clothing Store", "Comic Shop", "Farmers Market", "Gaming Cafe", "Massage Studio", "Winery", "Volcano", "Bay", "Athletics & Sports"];

	foods: string[] = ["Afghan Restaurant", "Ethiopian Restaurant", "American Restaurant", "Chinese Restaurant", "Filipino Restaurant", "Indonesian Restaurant", "Japanese Restaurant", "Korean Restaurant", "Mongolian Restaurant", "Australian Restaurant", "BBQ Joint", "Bubble Tea Shop", "Buffet", "Burget Joint", "Cajun / Creole Restaurant", "Caribbean Restaurant", "Coffee Shop", "Creperie", "Cupcake Shop", "Ice Cream Shop", "Donut Shop", "Falafel Restaurant", "Fast Food Restaurant", "Fish & Chips Shop", "French Restaurant", "Fried Chicken Joint", "German Restaurant", "Greek Restaurant", "Halal Restaurant", "Hawaiian Restaurant", "Indian Restaurant", "Indian Restaurant", "Mexican Restaurant", "Israeli Restaurant", "Persian Restaurant", "Lebanese Restaurant", "Pizza Place", "Russian Restaurant", "Sandwich Place", "Seafood Restaurant", "Bar"];

  constructor(private _formBuilder: FormBuilder, private http: HttpClient) { }

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
	this.url = 'http://0.0.0.0:5000/result?data=' + JSON.stringify(interests);
	console.log('first submit' + JSON.stringify(interests));
    
  }

  onFinalSubmit() {
  	this.http.get('http://0.0.0.0:5000/result?data={"interests":["Mini Golf","Clothing Store"],"food":["Burget Joint","Coffee Shop"]}').subscribe(data => {
  				this.res = data;
                
                for (let i = 0; i < this.res.data.length; i++) {
	            	this.finalInterests.push(this.res.data[i].name);
	            	this.finalLocations.push(this.res.data[i].location);
	            	this.latitudes.push(this.res.data[i].lat);
	            	this.longitudes.push(this.res.data[i].lng);
            	}
            
            });


  } 
 
  goUp(index: number) {
  	const temp = this.finalInterests[index - 1];
    this.finalInterests[index - 1] = this.finalInterests[index];
    this.finalInterests[index] = temp;

  }

  public options = {type : 'address', componentRestrictions: {  }};
getAddress(place: Address) {
    console.log('Address', place);
  }
  getFormattedAddress(event: any) {
    console.log(event);
    this.longitude = event.lng;
    this.latitude = event.lat;
  }


}
