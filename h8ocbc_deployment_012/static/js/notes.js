/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};
var url = window.location.href;
var newId = parseInt(url.substring(url.length - 1))
console.log(newId)

// Create the model instance
ns.model = (function () {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function (person_id) {
            let ajax_options = {
                type: 'GET',
                url: 'api/people/' + person_id,
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
        },
        create: function (content) {
            let ajax_options = {
                type: 'POST',
                url: `api/people/${newId}/notes`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'content': content
                })
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_create_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        update: function (note_id, content) {
            let ajax_options = {
                type: 'PUT',
                url: `api/people/${newId}/notes/${note_id}`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'content': content
                })
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_update_success', [data]);
                })
                .fail(function (xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        'delete': function (note_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `api/people/${newId}/notes/${note_id}`,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
                .done(function (data) {
                    $event_pump.trigger('model_delete_success', [data]);
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
    let $note_id = $('#note_id'),
        $content = $('#content');

    // return the API
    return {
        reset: function () {
            $note_id.val('');
            $content.val('').focus();
        },
        update_editor: function (note_id, content) {
            $note_id.val(note_id);
            $content.val(content).focus();
        },
        build_table: function (notes) {
            let rows = ''
            let banner = ''

            $('.banner').empty();

            // clear the table
            $('.notes table > tbody').empty();

            // did we get a people array?
            if (notes) {
                for (let i = 0, l = notes.notes.length; i < l; i++) {
                    rows += `<tr>
                                <td class="person_id">${notes.notes[i].person_id}</td>
                                <td class="note_id">${notes.notes[i].note_id}</td>
                                <td class="content">${notes.notes[i].content}</td>
                                <td>${notes.notes[i].timestamp}</td>
                            </tr>`;
                }
                banner += `<h1>${notes.fname} ${notes.lname}</h1>`
                $('table > tbody').append(rows);
                $('.banner').append(banner);
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
        $event_pump = $('body'),
        $note_id = $('#note_id'),
        $content = $('#content');

    // Get the data from the model after the controller is done initializing
    setTimeout(function () {
        console.log(url)
        model.read(newId);
    }, 100)

    // Validate input
    function validate(content) {
        return content !== "";
    }

    function validateId(note_id) {
        return note_id !== "";
    }

    // Create our event handlers
    $('#create').click(function (e) {
        let content = $content.val();

        e.preventDefault();

        if (validate(content)) {
            model.create(content)
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function (e) {
        let note_id = $note_id.val(),
            content = $content.val()

        e.preventDefault();

        if (validate(content) && validateId(note_id)) {
            model.update(note_id, content)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function (e) {
        let note_id = $note_id.val();

        e.preventDefault();

        if (validateId(note_id)) {
            model.delete(note_id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function () {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function (e) {
        let $target = $(e.target),
            note_id,
            content;

        note_id = parseInt($target
            .parent()
            .find('td.note_id')
            .text());

        content = $target
            .parent()
            .find('td.content')
            .text();
        console.log(note_id, content)
        console.log(typeof (note_id))
        view.update_editor(note_id, content);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function (e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function (e, data) {
        model.read(newId);
    });

    $event_pump.on('model_update_success', function (e, data) {
        model.read(newId);
    });

    $event_pump.on('model_delete_success', function (e, data) {
        model.read(newId);
    });

    $event_pump.on('model_error', function (e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));
