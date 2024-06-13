<?php
// Process form data and validation here

// Read the content of passing.txt file
$passingContent = file_get_contents('data/sem5/plans/passing.txt');

// Start session to store the content for the next page
session_start();
$_SESSION['passing_content'] = $passingContent;

// Redirect to the display plans page
header("Location: display_plans.html");
exit;
?>
