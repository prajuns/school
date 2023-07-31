var catAndActs = {};
catAndActs['Computer Science'] = ['Bsc', 'MCA', ];
catAndActs['Commerce'] = ['BBA', 'BCom'];
catAndActs['Electronics'] = ['Bsc', 'Msc', ];
catAndActs['Physics'] = ['Bsc', 'Msc','Phd' ];
catAndActs['Chemistry'] = ['Bsc', 'Msc','Phd' ];

function ChangecatList() {
    var catList = document.getElementById("validationCustom03");
    var actList = document.getElementById("validationCustom04");
    var selCat = catList.options[catList.selectedIndex].value;
    while (actList.options.length) {
        actList.remove(0);
    }
    var cats = catAndActs[selCat];
    if (cats) {
        var i;
        for (i = 0; i < cats.length; i++) {
            var cat = new Option(cats[i], i);
            actList.options.add(cat);
        }
    }
}