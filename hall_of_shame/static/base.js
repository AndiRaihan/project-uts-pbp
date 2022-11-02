async function getHallOfShame() {
    return fetch("json/").then((res) => res.json())
  }
  
  async function refreshHallOfShame() {
  
    const hallOfShameData = await getHallOfShame()
    let htmlString = ``
    hallOfShameData.forEach((item) => {
      var fields = item.fields
      var divCol = document.createElement("div");
      divCol.classList.add("col-md-3");
      divCol.style.cssText += 'padding-top: 15px;';
  
      var divCard = document.createElement("div");
      divCard.classList.add("card");
      divCard.classList.add("h-100");
  
      var divCardBody = document.createElement("div");
      divCardBody.classList.add("card-body");
      divCardBody.classList.add("d-flex");
      divCardBody.classList.add("flex-column");
  
      var cardName = document.createElement("h4");
      cardName.classList.add("card-title");
      cardName.innerHTML = fields.name
      divCardBody.appendChild(cardName);
  
      var cardDate = document.createElement("h6");
      cardDate.classList.add("card-title");
      cardDate.innerHTML = fields.created_date
      divCardBody.appendChild(cardDate);
  
      var cardArrestedDate = document.createElement("h6");
      cardArrestedDate.classList.add("card-text");
      cardArrestedDate.innerHTML = "Arrested on " + fields.arrested_date
      divCardBody.appendChild(cardArrestedDate);
  
      var cardCorruptType = document.createElement("h6");
      cardCorruptType.classList.add("card-text");
      cardCorruptType.innerHTML = "Corruption type: " + fields.corruption_type
      divCardBody.appendChild(cardCorruptType);
  
      var cardDesc = document.createElement("p");
      cardDesc.classList.add("card-text");
      cardDesc.innerHTML = fields.description

      divCardBody.appendChild(cardDesc);
  
      var divBtn = document.createElement("div");
      divBtn.classList.add("btn");
  
      var deleteBtn = document.createElement("button");
      deleteBtn.classList.add("delete-btn");
      deleteBtn.innerHTML = "Delete";
      deleteBtn.setAttribute('onclick', `deleteCorruptor(${item.pk})`);
      divBtn.appendChild(deleteBtn);
  
      divCardBody.appendChild(divBtn);
      divCard.appendChild(divCardBody);
      divCol.appendChild(divCard);
  
      htmlString += divCol.outerHTML
    });
  
    document.getElementById("cardContainer").innerHTML = htmlString;
  }
  
  function updateHallOfShame() {
    $.getJSON("json/", refreshHallOfShame);
  }
  
  function deleteCorruptor(pk) {
    $.ajax({
      url:`delete/${pk}/`,
      type: 'DELETE',
      success: updateHallOfShame,
    });
  }
  
  function addCorruptor() {
    fetch("add/", {
      method: "POST",
      body: new FormData(document.querySelector('#addCorruptorForm'))
    }).then(refreshHallOfShame)
    return false
  }
  
  document.getElementById("btn-submit").onclick = addCorruptor
  refreshHallOfShame()