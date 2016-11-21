<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <!--Import Google Icon Font-->
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <!--Custom css scripts go below this comment-->
    <link type="text/css" rel="stylesheet" href="css/style.css">
    


</head>

<body>
    <main>
        <?php
            include "static/header.php";
        ?>
        <div class="row">
        <div class="col s8 offset-s2">
        <!--Hérna Þarf að bætta bið Javascript kóða til að þetta verði Search-->
          <div class="row">
            <div class="input-field col s3">
              <input id="tableSearch" type="text" class="validate">
              <label for="tableSearch">Search</label>
            </div>
          </div>
         
         
                 <table id="table" class=" highlight">
                    <thead>
                      <tr>
                          <th data-field="id">Name</th>
                          <th data-field="name">Item Name</th>
                          <th data-field="price">Item Price</th>
                      </tr>
                    </thead>

                    <tbody>
                      <tr>
                        <td>Alvin</td>
                        <td>Eclair</td>
                        <td>$0.87</td>
                      </tr>
                      <tr>
                        <td>Alan</td>
                        <td>Jellybean</td>
                        <td>$3.76</td>
                      </tr>
                      <tr>
                        <td>Jonathan</td>
                        <td>Lollipop</td>
                        <td>$7.00</td>
                      </tr>
                    </tbody>
                    </table>
                </div>
        </div>
    </main>

    <!--Footer goes outside the main tag to make sure it stays on the bottom of the page-->
    <?php
        include "static/footer.php";
    ?>

    <!--Import jQuery before materialize.js-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>
    <!--Custom javascript files go below this comment-->
    <script src="javascript/start.js"></script>
    <script src="javascript/score.js"></script>
    <script type="text/javascript" src="javascript/jquery.tablesorter.js"></script> 

</body>
</html>