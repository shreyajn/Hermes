import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-interests-page',
  templateUrl: './interests-page.component.html',
  styleUrls: ['./interests-page.component.css']
})
export class InterestsPageComponent implements OnInit {

	interests: string[] = ["Aquarium", "Arcade", "Art Gallery", "Bowling Alley", "Casino", "Circus", "Comedy Club", "Concert Hall", "Go Kart Track", "Historic Site", "Karaoke Box", "Laser Tag", "Mini Golf", "Movie Theater", "Museum", "Jazz Club", "Opera House", "Theme Park", "Zoo", "Nightclub", "Lounge", "Gym / Fitness Center", "Beach", "Hot Spring", "Lake", "Lighthouse", "Mountain", "National Park", "Nature Preserve", "Park", "Rock Climbing Spot", "Trail", "Vineyard", "Waterfront", "Capitol Building", "Bookstore", "Candy Store", "Chocolate Shop", "Clothing Store", "Comic Shop", "Farmers Market", "Gaming Cafe", "Massage Studio", "Winery", "Volcano", "Bay", "Athletics & Sports"];

	food: string[] = ["Afghan Restaurant", "Ethiopian Restaurant", "American Restaurant", "Chinese Restaurant", "Filipino Restaurant", "Indonesian Restaurant", "Japanese Restaurant", "Korean Restaurant", "Mongolian Restaurant", "Australian Restaurant", "BBQ Joint", "Bubble Tea Shop", "Buffet", "Burget Joint", "Cajun / Creole Restaurant", "Caribbean Restaurant", "Coffee Shop", "Creperie", "Cupcake Shop", "Ice Cream Shop", "Donut Shop", "Falafel Restaurant", "Fast Food Restaurant", "Fish & Chips Shop", "French Restaurant", "Fried Chicken Joint", "German Restaurant", "Greek Restaurant", "Halal Restaurant", "Hawaiian Restaurant", "Indian Restaurant", "Indian Restaurant", "Mexican Restaurant", "Israeli Restaurant", "Persian Restaurant", "Lebanese Restaurant", "Pizza Place", "Russian Restaurant", "Sandwich Place", "Seafood Restaurant", "Bar"];

  constructor() { }

  ngOnInit() {
  }

}
