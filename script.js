window.onload = function () {
    function a(a, b) {
      var c = /^(?:file):/,
        d = new XMLHttpRequest(),
        e = 0;
      d.onreadystatechange = function () {
        4 == d.readyState && (e = d.status),
          c.test(location.href) && d.responseText && (e = 200),
          4 == d.readyState && 200 == e && (a.outerHTML = d.responseText);
      };
      try {
        d.open("GET", b, !0), d.send();
      } catch (f) {}
    }
    var b,
      c = document.getElementsByTagName("*");
    for (b in c)
      c[b].hasAttribute &&
        c[b].hasAttribute("data-include") &&
        a(c[b], c[b].getAttribute("data-include"));
  };




  function filterTable() {
    // Variables
    let dropdown, table, rows, cells, country, filter;
    dropdown = document.getElementById("ProductsDropdown");
    table = document.getElementById("myTable");
    rows = table.getElementsByTagName("tr");
    filter = dropdown.value;

    // Loops through rows and hides those with products that don't match the filter
    for (let row of rows) {
      // `for...of` loops through the NodeList
      cells = row.getElementsByTagName("td");
      country = cells[1] || null; // gets the 2nd `td` or nothing
      // if the filter is set to 'All', or this is the header row, or 2nd `td` text matches filter
      if (filter === "All" || !country || filter === country.textContent) {
        row.style.display = ""; // shows this row
      } else {
        row.style.display = "none"; // hides this row
      }
    }
  }







const getCellValue = (tr, idx) =>
        tr.children[idx].innerText || tr.children[idx].textContent;

      const comparer = (idx, asc) => (a, b) =>
        ((v1, v2) =>
          v1 !== "" && v2 !== "" && !isNaN(v1) && !isNaN(v2)
            ? v1 - v2
            : v1.toString().localeCompare(v2))(
          getCellValue(asc ? a : b, idx),
          getCellValue(asc ? b : a, idx)
        );

      // do the work...
      document.querySelectorAll("th").forEach((th) =>
        th.addEventListener("click", () => {
          const table = th.closest("table");
          Array.from(table.querySelectorAll("tr:nth-child(n+2)"))
            .sort(
              comparer(
                Array.from(th.parentNode.children).indexOf(th),
                (this.asc = !this.asc)
              )
            )
            .forEach((tr) => table.appendChild(tr));
        })
      );








      function myFunction() {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td")[0];
          if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
            } else {
              tr[i].style.display = "none";
            }
          }
        }
      }

