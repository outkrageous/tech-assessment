# tech-assessment
# PuppetLabs Perf/SDET Technical Evaluation Instructions #

Please use your time wisely to allow you to provide answers that demonstrate your strengths. Do your best to
complete the entire evaluation, but keep in mind that you may skip certain questions in order to give yourself
more time for others. Answer the questions in your own words.

For the scripting and programming questions you can use your language of choice or pseudo code. The scripting and
programming questions are evaluated for readability and effectiveness.

Our team is focused on understanding your thought process, experiences, and the way you went about determining the best
answer to each question. Please be prepared to discuss the evaluation questions and your answers later in
the interview process.

# General Linux #

1. How do you determine how much CPU is being utilized at the system level?

1. How do you determine how much CPU is being utilized by a specific process?

1. How would your answers to question 1 and 2 change if we were interested in looking at memory consumption?

1. How would your answers to question 1 and 2 change if we were interested in looking at disk or block input/output?

1. How would your answers to question 1 and 2 change if we were interested in looking at network utilization?

1. What is the difference between a process' virtual set size and resident set size? How does this affect the system as a whole?

1. What does strace do? How would you use it to debug a misbehaving process?

1. Name a utility you have used to do kernel level tracing.

1. How would you read a log file located in `/var/log/messages`?

1. If I told you to use the command `jabberwocky`, how can you find its
   documentation *without using Google?*

1. How do you redirect `stderr` and `stdout` to the same file?

1. How do you background a currently running long executing process?  How do you bring the process
   back to the foreground?

1. Given a log file located at `/var/log/mydaemon.log` which contains an
   indefinite number of lines like:

        Fri Jun 12 2014 12:00:01.345 user 'alice' logged in
        Fri Jun 12 2014 14:11:01.112 user 'bob' logged in
        Sun Jun 14 2014 00:11:01.112 ERROR: disk full
        Sun Jun 14 2014 01:05:10.100 ERROR: host is down
        Sun Jun 14 2014 08:33:33.333 successful backup

    How would you print the twenty most recently logged lines that contain error
 messages?

1. What is the purpose/use of `procfs`?  Where do you look to find `procfs`?

1. What are the steps for configuring and executing a passwordless login
   session to a remote Linux system?

# Networking #

1. What are important differences between TCP and UDP protocols?

1. Please provide basic troubleshooting steps for isolating connectivity
   problem between two Linux hosts, using only the shell.

1. How do you list a system's currently open ports and/or active connections?

# Development #

1. Why is it important to use software version control?

1. For a directory containing multiple files, implement a way to scan each file
   for the string "foobar" and replace it with "fubar"

1. How can you create 100 files named `000.pp` ... `099.pp` whose contents are (1 class per file):

        class myfile000 {
          if $kernel == "Linux" {
            file { '/tmp/myfile000':
              ensure  => file,
              backup  => false,
              content => "Hello myfile000",
            }
          }
        }

        ...

        class myfile099 {
          if $kernel == "Linux" {
            file { '/tmp/myfile099':
              ensure  => file,
              backup  => false,
              content => "Hello myfile099",
            }
          }
        }

# Programming #
1. Copy the CSV data below into a file

        Order #,Customer ID,Customer Name,Product SKU,Price,Purchase Date
        2887123,114,Roger McHammer,111-783,$34.32,05/12/2013
        2887124,115,Billy Balance,123-321,$22.12,05/12/2013
        2887125,22,Cody Conroy,112-777,$8.89,05/12/2013
        2887126,12,Steve Stevenson,109-009,$12.22,05/12/2013
        2887127,45,Colt Mustang Jr.,176-543,$16.82,05/12/2013
        2887128,32,Jill Ham,123-321,$22.12,05/12/2013
        2887129,90,Missy Mackle,111-783,$34.32,05/13/2013
        2887130,122,Combo Juarez,111-783,$34.32,05/13/2013
        2887131,22,Cody Conroy,176-543,$16.82,05/13/2013
        2887132,114,Roger McHammer,111-783,$34.32,05/13/2013
        2887133,115,Billy Balance,123-321,$22.12,05/14/2013
        2887134,24,Chet Baldry III,261-122,$109.11,05/14/2013
        2887135,33,Ken Washington,111-783,$34.32,05/14/2013
        2887136,151,Maria Melendez,222-333,$90.10,05/14/2013
        2887137,32,Jill Ham,111-784,$47.67,05/14/2013
        2887138,45,Colt Mustang Jr.,892-233,$78.32,05/15/2013
        2887139,114,Roger McHammer,111-784,$47.67,05/15/2013
        2887140,6,Jud Gofferton,678-903,$0.23,05/15/2013

    Create a program that will extract the data from the CSV file and perform the
 following operations:

    * Organize and sort the data by customer name.
    * Calculate the total number of orders per customer.
    * Calculate the average cost of orders per customer.

 Once the CSV has been loaded into a data model, create a report file containing
 the desired information from above in either JSON or XML format. You may use built-in
 JSON or XML libraries, and other built-in functions like sorting & searching in the language
 of your choice. (This includes using psuedocode.) You should provide your code as text in the same file as your previous answers.