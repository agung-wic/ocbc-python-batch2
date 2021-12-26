/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function () {
            let ajax_options = {
                type: 'GET',
                url: 'api/notes',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_read_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        }
    };
}());

// Create the view instance
ns.view = (function () {
    'use strict';

    // return the API
    return {
        build_table: function (notes) {
            let rows = ''

            // clear the table
            $('.notes table > tbody').empty();

            // did we get a people array?
            if (notes) {
                for (let i = 0, l = notes.length; i < l; i++) {
                    rows += `<tr>
                                <td class="person_id">${notes[i].person.person_id}</td>
                                <td class="name">${notes[i].person.fname} ${notes[i].person.lname}</td>
                                <td class="note_id">${notes[i].note_id}</td>
                                <td class="content">${notes[i].content}</td>
                                <td>${notes[i].timestamp}</td>
                            </tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function (error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function () {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function (m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body');

    // Get the data from the model after the controller is done initializing
    setTimeout(function () {
        model.read();
    }, 100)
    
    // Handle the model events
    $event_pump.on('model_read_success', function (e, data) {
        view.build_table(data);
    });

    $event_pump.on('model_error', function (e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));
