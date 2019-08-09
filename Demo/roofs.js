//import url from "/⁨Users⁩/nicolefavela⁩/Downloads⁩/Project⁩/dist⁩"
var select = document.getElementById("roofs")
    arr=["A-Frame","Regular","Vertical"]
    for(var i=0;i<arr.length;i++)
    {
        var option = document.createElement("OPTION"),
            txt=document.createTextNode(arr[i]);
            option.appendChild(txt);
            option.setAttribute("value",arr[i])
            select.insertBefore(option,select.lastChild);
            

    }
    
    //creates new image
    var img = new Image(300,300);
    function rf(){
        var r = document.getElementById("roofs").value;
        if (r == "Regular"){
            img.src='regstyle_prices.png';
            document.body.appendChild(img);
        }
        else if (r == "A-Frame"){
            img.src='a-frame.png';
            document.body.appendChild(img);

        }
        else{
            img.src='vertical_roof_style.png';
            document.body.appendChild(img);

        }
       
    }

    


