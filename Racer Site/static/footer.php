<?php
/**
 * By: Alexander
 * Date: 19-Nov-16
 * Time: 1:18 AM
 * Description: This is the static footer for the website
 */
?>
<footer class="page-footer cyan darken-4">
        <div class="container">
            <div class="row">
                <div class="col l6 s12">
                    <h5 class="white-text">Racer co.</h5>
                    <p class="grey-text text-lighten-4">
                        Contact us at
                        <a href="mailto:vorur.mail@gmail.com" class="grey-text text-lighten-3">
                            vorur.mail@gmail.com
                        </a>
                        to get in touch!</p>
                </div>
                <div class="col l4 offset-l2 s12">
                    <h5 class="white-text">This project is powered by</h5>
                    <ul class="section">
                        <li class="git"><a class="grey-text text-lighten-3" href="https://github.com/AlexKnows/Racer_final_project"><i class="fa fa-github" aria-hidden="true"></i> Github</a></li>
                        <li class="met"><a class="grey-text text-lighten-3" href="http://materializecss.com/"><i class="fa fa-code" aria-hidden="true"></i> Materialize</a></li>
                        <li class="python"><a class="grey-text text-lighten-3" href="https://python.org"><i class="fa fa-pied-piper" aria-hidden="true"></i> Python</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-copyright">
            <div class="container">
                &copy;<?php
            $startYear = 2016;
            $thisYear = date("Y");
            if ($startYear == $thisYear) {
             echo $startYear;
            } else {
             echo "{$startYear}&ndash;{$thisYear}";
            }
            ?> Racer Inc.
            </div>
        </div>
    </footer>

