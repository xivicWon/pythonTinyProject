from enum import Enum 
class QueryType(Enum):
    Keyword = "Keyword"
    Title = "Title"
    Author= "Author"
    Publisher = "Publisher"

class SearchTarget(Enum):
    Book = "Book"
    Foreign = "Foreign"
    Music= "Music"
    DVD = "DVD"
    Used = "Used"
    eBook = "eBook"
    All = "All"


class Sort(Enum):
    Accuracy = "Accuracy"
    PublishTime = "PublishTime"
    Title= "Title"
    SalesPoint = "SalesPoint"
    CustomerRating = "CustomerRating"
    MyReviewCount = "MyReviewCount"


class Cover(Enum):
    Big = "Big"
    MidBig = "MidBig"
    Mid= "Mid"
    Small = "Small"
    Mini = "Mini"

class OutputType(Enum):
    XML = "xml"
    JSON = "js"
