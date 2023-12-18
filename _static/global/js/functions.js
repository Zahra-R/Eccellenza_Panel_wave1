
function old() {
    // Get all table rows
    var rows = document.querySelectorAll('.radiotable tr');

    // Initialize min width variable
    var minTableWidth = 0;

    // Iterate over each row
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first one
        var cells = row.querySelectorAll('th:not(:first-child), td:not(:first-child)');
        // Iterate over each cell in the row
        cells.forEach(function(cell) {
            // Get the content of the cell
            var content = cell.textContent || cell.innerText;

            // Split the content into words
            var words = content.split(/\s+/);

            // Find the length of the longest word
            var maxLength = Math.max(...words.map(word => word.length));

            // Update the min width for the entire table
            minTableWidth = Math.max(minTableWidth, maxLength);
        });
        
    });

    // Apply the min width to each column (excluding the first one)
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first one
        var cells = row.querySelectorAll('th:not(:first-child), td:not(:first-child)');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
            if(minTableWidth>=5){
                cell.style.maxWidth = 6 + 'ch';
                cell.style.minWidth = 6 + 'ch';
                console.log("is small")
            }
            else {
                cell.style.maxWidth = 6 + 'ch';
                cell.style.minWidth = 6 + 'ch';
                console.log("is large")
            }
            
        });
    });
}

function old2() {
    // Get all table rows
    var rows = document.querySelectorAll('.radiotable tr');

    // Initialize min width
    var minTableWidth = 0;

    // Iterate over each row
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first and second ones
        var cells = row.querySelectorAll('th:not(:nth-child(1)):not(:nth-child(2)), td:not(:nth-child(1)):not(:nth-child(2))');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
            // Get the content of the cell
            var content = cell.textContent || cell.innerText;

            // Split the content into words
            var words = content.split(/\s+/);

            // Find the length of the longest word
            var maxLength = Math.max(...words.map(word => word.length));

            // Update the min width
            minTableWidth = Math.max(minTableWidth, maxLength);
        });
    });

    // Apply the min width to each column (excluding the first and second ones)
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first and second ones
        var cells = row.querySelectorAll('th:not(:nth-child(1)):not(:nth-child(2)), td:not(:nth-child(1)):not(:nth-child(2))');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
            if(minTableWidth>=5){
                cell.style.maxWidth = 6 + 'ch';
                cell.style.minWidth = 6 + 'ch';
            }
            else {
                cell.style.minWidth = minTableWidth + 'ch';
            }
        });
    });
}


function setWidthForTableColumns3() {
    var rows = document.querySelectorAll('.radiotable tr');
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first one
        var cells = row.querySelectorAll('th:not(:first-child), td:not(:first-child)');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
                cell.style.maxWidth = 10 + 'ch';
                cell.style.minWidth = 10 + 'ch';
            
        });
    });
}


function setWidthForTableColumns1() {
    var rows = document.querySelectorAll('.radiotable tr');
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first one
        var cells = row.querySelectorAll('th:not(:first-child), td:not(:first-child)');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
                cell.style.maxWidth = 6 + 'ch';
                cell.style.minWidth = 6 + 'ch';
            
        });
    });
}


function setWidthForTableColumns7() {
    var rows = document.querySelectorAll('.radiotable tr');
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first one
        var cells = row.querySelectorAll('th:not(:first-child), td:not(:first-child)');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
                cell.style.maxWidth = 7 + 'ch';
                cell.style.minWidth = 7 + 'ch';
            
        });
    });
}


function setWidthForTableColumns2() {
    var rows = document.querySelectorAll('.radiotable tr');
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first and second ones
        var cells = row.querySelectorAll('th:not(:nth-child(1)):not(:nth-child(2)), td:not(:nth-child(1)):not(:nth-child(2))');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
                cell.style.maxWidth = 6 + 'ch';
                cell.style.minWidth = 6 + 'ch';
            
        });
    });
}


function setWidthForTableColumns4() {
    var rows = document.querySelectorAll('.radiotable tr');
    rows.forEach(function(row) {
        // Get all cells in the row, excluding the first and second ones
        var cells = row.querySelectorAll('th:not(:nth-child(1)):not(:nth-child(2)), td:not(:nth-child(1)):not(:nth-child(2))');

        // Iterate over each cell in the row
        cells.forEach(function(cell) {
                cell.style.maxWidth = 5 + 'ch';
                cell.style.minWidth = 5 + 'ch';
            
        });
    });
}
console.log("Check!");