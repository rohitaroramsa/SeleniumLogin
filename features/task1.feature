Feature: Open Google.com and Search various Objects

Scenario Outline: Google.com can be browsed and searched upon
Given A Chrome Browser
When user browses site "http://google.com"
and user enters "<cityname>"
and user clicks on Search button
Then the search result Page should open
and screenshot shall be taken
Examples:
|cityname|
|Bahamas|
|Amsterdam|