from pyscript import document

def candidate_checker(e):
    club_members = {"gabby gregorio" , "jade saquido", "yoninah lim", "jilliane singh", "ciana dicka"}

    f_name = document.getElementById('first name').value
    l_name = document.getElementById('last name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.' ,
               f'Congratulations! {candidate}, you are part of the dance club.')

document.getElementById("result").innerHTML = messages [member_checker]