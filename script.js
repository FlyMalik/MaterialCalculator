// Definition function that activate parameters
function activate(){
let lengthIN = parseFloat(document.getElementById("lgt_entry").value) 
let widthIN = parseFloat(document.getElementById("wdt_entry").value)
let depthIN = parseFloat(document.getElementById("dpt_entry").value)
let cementIN = parseFloat(document.getElementById("cmt_entry" ).value)
let sandIN = parseFloat(document.getElementById("snd_entry").value)
let graniteIN = parseFloat(document.getElementById("grn_entry").value)

// Entries and Outputs
let cubic = lengthIN * widthIN * depthIN
let dimension = cubic
let total_ratio = cementIN + sandIN + graniteIN
let cement_co = cementIN / total_ratio
let sand_co = sandIN / total_ratio
let granite_co = graniteIN / total_ratio

// Constants
let cement_factor = 1440
let sand_factor = 1450
let granite_factor = 1550
let k2 = 50
let k3 = 1000
let wastagePercent = 0.05

// Cement
let cement1 = cement_co * dimension
let cement2 = cement1 * cement_factor
let cement3 = cement2 / k2
let cement_final1 = cement3
let cement_final2 = cement_final1 * wastagePercent
let cement_final3 = cement_final2 + cement_final1
let cement_final = cement_final3.toFixed(2)


// Sand
let sand1 = sand_co * dimension
let sand2 = sand1 * sand_factor
let sand3 = sand2 / k3
let sand_final1 = sand3
let sand_final2 = sand_final1 * wastagePercent
let sand_final3 = sand_final2 + sand_final1 
let sand_final = sand_final3.toFixed(2)


// Granite
let granite1 = granite_co * dimension
let granite2 = granite1 * granite_factor
let granite3 = granite2 / k3
let granite_final1 = granite3
let granite_final2 = granite_final1 * wastagePercent
let granite_final3 = granite_final2 + granite_final1
let granite_final = granite_final3.toFixed(2)



// Display 
cementOUT.textContent = cement_final
sandOUT.textContent = sand_final
graniteOUT.textContent = granite_final
dimensionOUT.textContent = dimension + ' meter cube'


// if (cementOUT.textContent === nada | sandOUT.textContent=== nada | graniteOUT.textContent === nada) {
//     feedbackOUT2.innerHTML = 'Invalid or Incomplete entry. Please check. Reset program and enter only numbers. Thank you'
// }
// else {feedbackOUT2.innerHTML = 'Succesful Calculation. Thank you for using this Program.'}

if (isNaN(cementOUT.textContent))
{
        feedbackOUT2.innerHTML = 'Invalid or Incomplete entry. Please check. Reset program and enter only numbers. Thank you'
        cementOUT.textContent = '*^%$#@'
     sandOUT.textContent = '*^%$#@'
     graniteOUT.textContent = '*^%$#@'
     dimensionOUT.textContent = '*^%$#@'
   

    }

else {feedbackOUT2.innerHTML = 'Succesful Calculation. Thank you for using this Program. Reset to begin again.'
        percOUT1.textContent = '*Already added: additional 5% for wastage'
        percOUT2.textContent = '*Already added: additional 5% for wastage'
        percOUT3.textContent = '*Already added: additional 5% for wastage'
}    

}



let dimensionOUT = document.getElementById("dim_entry")
let cementOUT = document.getElementById("bag_entry2")
let sandOUT = document.getElementById("tnS_entry")
let graniteOUT = document.getElementById("tnG_entry")
let feedbackOUT2 = document.getElementById("fdb_entry2")
let percOUT1 = document.getElementById('perc1')
let percOUT2 = document.getElementById('perc2')
let percOUT3 = document.getElementById('perc3')


feedbackOUT2.innerHTML = "Hello user, enter only numbers in the spaces provided"
cementOUT.textContent = " "
percOUT1.textContent = ''
percOUT2.textContent = ''
percOUT3.textContent = ''




// functions
function calculate(){
activate()
}

function reset(){
    cementOUT.textContent = ""
    sandOUT.textContent = ""
    graniteOUT.textContent = ""
    dimensionOUT.textContent = ""

    let lengthIN = document.getElementById("lgt_entry") 
    let widthIN = document.getElementById("wdt_entry")
    let depthIN = document.getElementById("dpt_entry")
    let cementIN = document.getElementById("cmt_entry" )
    let sandIN = document.getElementById("snd_entry")
    let graniteIN = document.getElementById("grn_entry")

     lengthIN.value= ''
     widthIN.value = ''
     depthIN.value = ''
     cementIN.value = ''
     sandIN.value = ''
     graniteIN.value = ''
     cementOUT.textContent = " "
     percOUT1.textContent = ''
     percOUT2.textContent = ''
     percOUT3.textContent = ''
     
     feedbackOUT2.innerHTML = "Hello user, enter only numbers in the spaces provided"
}
