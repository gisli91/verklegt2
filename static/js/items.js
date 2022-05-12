$(document).ready(function () {
    $('#search-btn').on("click", function (e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax(  {
            url: "/items?search_filter=" + searchText,
            type: "GET",
            success: function(resp) {
                let newHTML = resp.data.map(d => {
                    return `<div class="col-sm-4 col-md-6 col-lg-4 d-flex align-items-stretch">
                            <a href="/items/${ d.id }">
                                    <div class="card" style="width: 18rem;">
                                         <img class="card-img-top" src="${ d.image }">
                                         <div class="card-body">
                                            <h5 class="card-title">${ d.name }</h5>
                                            <p class="card-text">${ d.highest_bid }$</p>
                                            <p class="card-text"><small class="text-muted">${ d.seller }</small></p>
                                            <p class="card-text"><small class="text-muted">Category: ${ d.category } </small></p>
                                         </div>
                                    </div>
                                </a>
                                </div>`
                    });

                    $(".items").html(newHTML.join(""))
                    $('#search-box').val("")
                },
                error: function (xhr, status, error) {
                    console.error(error);
                }
            })

        });

    $('#sort-price-btn').on("click", function (e) {
        e.preventDefault();
        $.ajax(  {
            url: "/items?sort_price_filter=True" ,
            type: "GET",
            success: function(resp) {
                let newHTML = resp.data.map(d => {
                    return `<div class="col-sm-4 col-md-6 col-lg-4 d-flex align-items-stretch">
                                <a href="/items/${ d.id }">
                                    <div class="card" style="width: 18rem;">
                                         <img class="card-img-top" src="${ d.image }">
                                         <div class="card-body">
                                            <h5 class="card-title">${ d.name }</h5>
                                            <p class="card-text">${ d.highest_bid }$</p>
                                            <p class="card-text"><small class="text-muted">${ d.seller }</small></p>
                                            <p class="card-text"><small class="text-muted">Category: ${ d.category } </small></p>
                                         </div>
                                    </div>
                                </a>
                            </div>`
                    });

                    $(".items").html(newHTML.join(""))
                },
                error: function (xhr, status, error) {
                    console.error(error);
                }
            })

        });

});

