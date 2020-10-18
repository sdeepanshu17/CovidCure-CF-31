from tkinter import *
from PIL import ImageTk
import mysql.connector as con

def bye():
    quit()


def home():

    global root
    root = Tk()
    root.title("COVID HELPLINE ")
    root.geometry("1300x750")
    root.resizable(False, False)

    bg = ImageTk.PhotoImage(file = "img.png")       
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )

    l1 = Label(root, fg='black',bg="#adffe3", font=("Bebas Neue", 30, "bold"), text="Welcome to COVID-19 HELPLINE")     
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file="corona.png")  
    #Label(root, image=bgg,borderwidth=0).place(x=30)

    root.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file="Images\stats.jpg")      
    Label(root, image=bg1).place(x=120, y=82)

    b1 = Button(root, text="No. of Cases", font=('Roboto', 14),bd=0.1, command=data, bg='white', fg='black')
    b1.place(x=250, y=342, height=40, width=262)
    def entered(event):
        b1.config( bg="grey",fg="black")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)

    


    bg2 = ImageTk.PhotoImage(file="Images\info.jpg")    
    Label(root, image=bg2).place(x=650, y=82)
    

    b2 = Button(root, text="Information",command=info, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b2.place(x=780, y=342, height=40, width=262)
    def entered1(event):
        b2.config( bg="grey",fg="black")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)



    bg3 = ImageTk.PhotoImage(file="Images\donatee.jpg")      
    Label(root, image=bg3).place(x=120, y=392)

    b3 = Button(root, text="Donation Center",command=donate, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b3.place(x=250, y=652, height=40, width=262)
    def entered2(event):
        b3.config( bg="grey",fg="black")
    def left2(event):
        b3.config(bg="white",fg="black")
    b3.bind("<Enter>",entered2)
    b3.bind("<Leave>",left2)

    bg4 = ImageTk.PhotoImage(file="Images/assist.jpg")      
    Label(root, image=bg4).place(x=650, y=392)

    b4 = Button(root, text="Medical Assist",command=m_assist, font=('Roboto', 14),bd=0.1, bg='white', fg='black')
    b4.place(x=780, y=652, height=40, width=262)
    def entered3(event):
        b4.config( bg="grey",fg="black")
    def left3(event):
        b4.config(bg="white",fg="black")
    b4.bind("<Enter>",entered3)
    b4.bind("<Leave>",left3)


    bg5 = ImageTk.PhotoImage(file="Images/corona.png")      
    Label(root, image=bg5).place(x=560, y=302)

    b5=Button(root, text='Exit', command=bye,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    root.mainloop()



def revert2():
    root2.destroy()
    home()

def revert3():
    root3.destroy()
    home()

def revert4():
    root4.destroy()
    home()

def revert5():
    root5.destroy()
    home()

def revert6():
    root6.destroy()
    home()




def data():

    root.destroy()

    global root2

    root2 = Tk()
    root2.title("Number of Covid-19 Cases")
    root2.geometry("1300x750")
    root2.resizable(False, False)
    
    bg5 = ImageTk.PhotoImage(file=r"sbg8.png")  # BACKGROUND IMAGE
    Label(root2, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)


    l1 = Label(root2, fg='black',bg="#adffe3", font=("Bebas Neue", 30, "bold"), text="COVID-DATA")     
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"corona.png")  

    root2.iconphoto(False, bgg)

    var = StringVar(root2)
    var.set("Select City")

    import requests

    url = "https://rapidapi.p.rapidapi.com/api_india"

    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "d66054e6d4msha2e0c1420b1196fp1d9340jsn28edd953ccc0"
        }

    response = requests.request("GET", url, headers=headers).json()

    def search_by_city(city_name_input):
        for each in response['state_wise']:
            if int(response["state_wise"][each]["active"]) != 0:
                for city in response['state_wise'][each]['district']:
                    if city==city_name_input:
                        return response['state_wise'][each]['district'][city]['active'] 
    def search_by_city_deaths(city_name_input):
        for each in response['state_wise']:
        
            for city in response['state_wise'][each]['district']:
                if city==city_name_input:
                    return response['state_wise'][each]['district'][city]['deceased'] 

    def search_by_city_recovred(city_name_input):
        for each in response['state_wise']:
            if int(response["state_wise"][each]["recovered"]) != 0:
                for city in response['state_wise'][each]['district']:
                    if city==city_name_input:
                        return response['state_wise'][each]['district'][city]['recovered']
    def out():
        global cases
        global deaths
        global recovred
        cityname=chosen_option
        cityname=cityname.capitalize()    
        cases=search_by_city(cityname)
        deaths=search_by_city_deaths(cityname)
        recovred=search_by_city_recovred(cityname)

        


    def grab_and_assign(event):
        global chosen_option
        chosen_option = var.get()
        out()
        l3= Label(root2, text=chosen_option, font=("Roboto", 40,'bold' ))
        l3.place(x=150, y=200)
        l3.config(width=18)
        l4= Label(root2, text="Active Cases: "+str(cases), font=("Roboto", 30))
        l4.place(x=190, y=280)
        l4.config(width=20)
        l5= Label(root2, text="Recovered Cases: "+str(recovred), font=("Roboto", 30 ))
        l5.place(x=190, y=350)
        l5.config(width=20)
        l6= Label(root2, text="Deaths: "+str(deaths), font=("Roboto", 30 ))
        l6.place(x=190, y=420)
        l6.config(width=20)


        
        if cases==None:
            Label(root2, image=i3).place(x=800, y=220)
        elif int(cases)>5000:
            Label(root2, image=i1).place(x=800, y=220)
        
        elif 5000>int(cases)>1000:
            Label(root2, image=i2).place(x=800, y=220)

        elif 1000>int(cases):
            Label(root2, image=i3).place(x=800, y=220)
        else:
            Label(root2, image=i3).place(x=750, y=220)


    i1=ImageTk.PhotoImage(file="Images/danger.png")
    i2=ImageTk.PhotoImage(file="Images/risky.png")
    i3=ImageTk.PhotoImage(file="Images/low.png")

    l2 = Label(root2, font=("Bebas Neue", 30, "bold"), text="Select a City:")     
    l2.place(x=100, y=100)
    drop_menu = OptionMenu(root2, var, 'Adilabad', 'Agar Malwa', 'Agra', 'Ahmedabad', 'Ahmednagar', 'Airport Quarantine', 'Airport Quarantine', 'Aizawl', 'Ajmer', 'Akola', 'Alappuzha', 'Aligarh', 'Alipurduar', 'Alirajpur', 'Almora', 'Alwar', 'Ambala', 'Ambedkar Nagar', 'Amethi', 'Amravati', 'Amreli', 'Amritsar', 'Amroha', 'Anand', 'Anantapur', 'Anantnag', 'Angul', 'Anjaw', 'Anuppur', 'Araria', 'Aravalli', 'Ariyalur', 'Arwal', 'Ashoknagar', 'Auraiya', 'Aurangabad', 'Aurangabad', 'Ayodhya', 'Azamgarh', 'BSF Camp', 'Bagalkote', 'Bageshwar', 'Baghpat', 'Bahraich', 'Baksa', 'Balaghat', 'Balangir', 'Balasore', 'Ballari', 'Ballia', 'Balod', 'Baloda Bazar', 'Balrampur', 'Balrampur', 'Bametara', 'Banaskantha', 'Banda', 'Bandipora', 'Banka', 'Bankura', 'Banswara', 'Barabanki', 'Baramulla', 'Baran', 'Bareilly', 'Bargarh', 'Barmer', 'Barnala', 'Barpeta', 'Barwani', 'Bastar', 'Basti', 'Bathinda', 'Beed', 'Begusarai', 'Belagavi', 'Bengaluru Rural', 'Bengaluru Urban', 'Betul', 'Bhadohi', 'Bhadradri Kothagudem', 'Bhadrak', 'Bhagalpur', 'Bhandara', 'Bharatpur', 'Bharuch', 'Bhavnagar', 'Bhilwara', 'Bhind', 'Bhiwani', 'Bhojpur', 'Bhopal', 'Bidar', 'Bijapur', 'Bijnor', 'Bikaner', 'Bilaspur', 'Bilaspur', 'Birbhum', 'Bishnupur', 'Biswanath', 'Bokaro', 'Bongaigaon', 'Botad', 'Boudh', 'Budaun', 'Budgam', 'Bulandshahr', 'Buldhana', 'Bundi', 'Burhanpur', 'Buxar', 'CAPF Personnel', 'Cachar', 'Central Delhi', 'Chamarajanagara', 'Chamba', 'Chamoli', 'Champawat', 'Champhai', 'Chandauli', 'Chandel', 'Chandigarh', 'Chandrapur', 'Changlang', 'Charaideo', 'Charkhi Dadri', 'Chatra', 'Chengalpattu', 'Chennai', 'Chhatarpur', 'Chhindwara', 'Chhota Udaipur', 'Chikkaballapura', 'Chikkamagaluru', 'Chirang', 'Chitradurga', 'Chitrakoot', 'Chittoor', 'Chittorgarh', 'Churachandpur', 'Churu', 'Coimbatore', 'Cooch Behar', 'Cuddalore', 'Cuttack', 'Dadra and Nagar Haveli', 'Dahod', 'Dakshin Bastar Dantewada', 'Dakshin Dinajpur', 'Dakshina Kannada', 'Daman', 'Damoh', 'Dang', 'Darbhanga', 'Darjeeling', 'Darrang', 'Datia', 'Dausa', 'Davanagere', 'Dehradun', 'Deogarh', 'Deoghar', 'Deoria', 'Devbhumi Dwarka', 'Dewas', 'Dhalai', 'Dhamtari', 'Dhanbad', 'Dhar', 'Dharmapuri', 'Dharwad', 'Dhemaji', 'Dhenkanal', 'Dholpur', 'Dhubri', 'Dhule', 'Dibrugarh', 'Dima Hasao', 'Dimapur', 'Dindigul', 'Dindori', 'Diu', 'Doda', 'Dumka', 'Dungarpur', 'Durg', 'East Champaran', 'East Delhi', 'East Garo Hills', 'East Godavari', 'East Jaintia Hills', 'East Kameng', 'East Khasi Hills', 'East Siang', 'East Sikkim', 'East Singhbhum', 'Ernakulam', 'Erode', 'Etah', 'Etawah', 'Evacuees', 'Faridabad', 'Faridkot', 'Farrukhabad', 'Fatehabad', 'Fatehgarh Sahib', 'Fatehpur', 'Fazilka', 'Ferozepur', 'Firozabad', 'Foreign Evacuees', 'Foreign Evacuees', 'Foreign Evacuees', 'Gadag', 'Gadchiroli', 'Gajapati', 'Ganderbal', 'Gandhinagar', 'Ganganagar', 'Ganjam', 'Garhwa', 'Gariaband', 'Gaurela Pendra', 'Gautam Buddha Nagar', 'Gaya', 'Ghaziabad', 'Ghazipur', 'Gir Somnath', 'Giridih', 'Goalpara', 'Godda', 'Golaghat', 'Gomati', 'Gonda', 'Gondia', 'Gopalganj', 'Gorakhpur', 'Gumla', 'Guna', 'Guntur', 'Gurdaspur', 'Gurugram', 'Gwalior', 'Hailakandi', 'Hamirpur', 'Hamirpur', 'Hanumangarh', 'Hapur', 'Harda', 'Hardoi', 'Haridwar', 'Hassan', 'Hathras', 'Haveri', 'Hazaribagh', 'Hingoli', 'Hisar', 'Hnahthial', 'Hojai', 'Hooghly', 'Hoshangabad', 'Hoshiarpur', 'Howrah', 'Hyderabad', 'Idukki', 'Imphal East', 'Imphal West', 'Indore', 'Italians', 'Italians', 'Jabalpur', 'Jagatsinghpur', 'Jagtial', 'Jaipur', 'Jaisalmer', 'Jajpur', 'Jalandhar', 'Jalaun', 'Jalgaon', 'Jalna', 'Jalore', 'Jalpaiguri', 'Jammu', 'Jamnagar', 'Jamtara', 'Jamui', 'Jangaon', 'Janjgir Champa', 'Jashpur', 'Jaunpur', 'Jayashankar Bhupalapally', 'Jehanabad', 'Jhabua', 'Jhajjar', 'Jhalawar', 'Jhansi', 'Jhargram', 'Jharsuguda', 'Jhunjhunu', 'Jind', 'Jiribam', 'Jodhpur', 'Jogulamba Gadwal', 'Jorhat', 'Junagadh', 'Kabeerdham', 'Kaimur', 'Kaithal', 'Kakching', 'Kalaburagi', 'Kalahandi', 'Kalimpong', 'Kallakurichi', 'Kamareddy', 'Kamjong', 'Kamle', 'Kamrup', 'Kamrup Metropolitan', 'Kancheepuram', 'Kandhamal', 'Kangpokpi', 'Kangra', 'Kannauj', 'Kannur', 'Kanpur Dehat', 'Kanpur Nagar', 'Kanyakumari', 'Kapurthala', 'Karaikal', 'Karauli', 'Karbi Anglong', 'Kargil', 'Karimganj', 'Karimnagar', 'Karnal', 'Karur', 'Kasaragod', 'Kasganj', 'Kathua', 'Katihar', 'Katni', 'Kaushambi', 'Kendrapara', 'Kendujhar', 'Khagaria', 'Khammam', 'Khandwa', 'Khargone', 'Khawzawl', 'Kheda', 'Khordha', 'Khowai', 'Khunti', 'Kinnaur', 'Kiphire', 'Kishanganj', 'Kishtwar', 'Kodagu', 'Koderma', 'Kohima', 'Kokrajhar', 'Kolar', 'Kolasib', 'Kolhapur', 'Kolkata', 'Kollam', 'Komaram Bheem', 'Kondagaon', 'Koppal', 'Koraput', 'Korba', 'Koriya', 'Kota', 'Kottayam', 'Kozhikode', 'Kra Daadi', 'Krishna', 'Krishnagiri', 'Kulgam', 'Kullu', 'Kupwara', 'Kurnool', 'Kurukshetra', 'Kurung Kumey', 'Kushinagar', 'Kutch', 'Lahaul and Spiti', 'Lakhimpur', 'Lakhimpur Kheri', 'Lakhisarai', 'Lalitpur', 'Latehar', 'Latur', 'Lawngtlai', 'Leh', 'Lepa Rada', 'Lohardaga', 'Lohit', 'Longding', 'Longleng', 'Lower Dibang Valley', 'Lower Siang', 'Lower Subansiri', 'Lucknow', 'Ludhiana', 'Lunglei', 'Madhepura', 'Madhubani', 'Madurai', 'Mahabubabad', 'Mahabubnagar', 'Maharajganj', 'Mahasamund', 'Mahe', 'Mahendragarh', 'Mahisagar', 'Mahoba', 'Mainpuri', 'Majuli', 'Malappuram', 'Malda', 'Malkangiri', 'Mamit', 'Mancherial', 'Mandi', 'Mandla', 'Mandsaur', 'Mandya', 'Mansa', 'Marwahi', 'Mathura', 'Mau', 'Mayurbhanj', 'Medak', 'Medchal Malkajgiri', 'Meerut', 'Mehsana', 'Mirpur', 'Mirzapur', 'Moga', 'Mokokchung', 'Mon', 'Moradabad', 'Morbi', 'Morena', 'Morigaon', 'Mulugu', 'Mumbai', 'Mumbai Suburban', 'Mungeli', 'Munger', 'Murshidabad', 'Muzaffarabad', 'Muzaffarnagar', 'Muzaffarpur', 'Mysuru', 'Nabarangapur', 'Nadia', 'Nagaon', 'Nagapattinam', 'Nagarkurnool', 'Nagaur', 'Nagpur', 'Nainital', 'Nalanda', 'Nalbari', 'Nalgonda', 'Namakkal', 'Namsai', 'Nanded', 'Nandurbar', 'Narayanpet', 'Narayanpur', 'Narmada', 'Narsinghpur', 'Nashik', 'Navsari', 'Nawada', 'Nayagarh', 'Neemuch', 'New Delhi', 'Nicobars', 'Nilgiris', 'Nirmal', 'Niwari', 'Nizamabad', 'Noney', 'North 24 Parganas', 'North Delhi', 'North East Delhi', 'North Garo Hills', 'North Goa', 'North Sikkim', 'North Tripura', 'North West Delhi', 'North and Middle Andaman', 'Nuapada', 'Nuh', 'Osmanabad', 'Other Region', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Other State', 'Others', 'Others', 'Pakke Kessang', 'Pakur', 'Palakkad', 'Palamu', 'Palghar', 'Pali', 'Palwal', 'Panchkula', 'Panchmahal', 'Panipat', 'Panna', 'Papum Pare', 'Parbhani', 'Paschim Bardhaman', 'Paschim Medinipur', 'Patan', 'Pathanamthitta', 'Pathankot', 'Patiala', 'Patna', 'Pauri Garhwal', 'Peddapalli', 'Perambalur', 'Peren', 'Phek', 'Pherzawl', 'Pilibhit', 'Pithoragarh', 'Porbandar', 'Prakasam', 'Pratapgarh', 'Pratapgarh', 'Prayagraj', 'Puducherry', 'Pudukkottai', 'Pulwama', 'Punch', 'Pune', 'Purba Bardhaman', 'Purba Medinipur', 'Puri', 'Purnia', 'Purulia', 'Rae Bareli', 'Raichur', 'Raigad', 'Raigarh', 'Railway Quarantine', 'Raipur', 'Raisen', 'Rajanna Sircilla', 'Rajgarh', 'Rajkot', 'Rajnandgaon', 'Rajouri', 'Rajsamand', 'Ramanagara', 'Ramanathapuram', 'Ramban', 'Ramgarh', 'Rampur', 'Ranchi', 'Ranga Reddy', 'Ranipet', 'Ratlam', 'Ratnagiri', 'Rayagada', 'Reasi', 'Rewa', 'Rewari', 'Ribhoi', 'Rohtak', 'Rohtas', 'Rudraprayag', 'Rupnagar', 'S.A.S. Nagar', 'S.P.S. Nellore', 'Sabarkantha', 'Sagar', 'Saharanpur', 'Saharsa', 'Sahibganj', 'Saiha', 'Saitual', 'Salem', 'Samastipur', 'Samba', 'Sambalpur', 'Sambhal', 'Sangareddy', 'Sangli', 'Sangrur', 'Sant Kabir Nagar', 'Saraikela-Kharsawan', 'Saran', 'Satara', 'Satna', 'Sawai Madhopur', 'Sehore', 'Senapati', 'Seoni', 'Serchhip', 'Shahdara', 'Shahdol', 'Shahid Bhagat Singh Nagar', 'Shahjahanpur', 'Shajapur', 'Shamli', 'Sheikhpura', 'Sheohar', 'Sheopur', 'Shi Yomi', 'Shimla', 'Shivamogga', 'Shivpuri', 'Shopiyan', 'Shrawasti', 'Siang', 'Siddharthnagar', 'Siddipet', 'Sidhi', 'Sikar', 'Simdega', 'Sindhudurg', 'Singrauli', 'Sipahijala', 'Sirmaur', 'Sirohi', 'Sirsa', 'Sitamarhi', 'Sitapur', 'Sivaganga', 'Sivasagar', 'Siwan', 'Solan', 'Solapur', 'Sonbhadra', 'Sonipat', 'Sonitpur', 'South 24 Parganas', 'South Andaman', 'South Delhi', 'South East Delhi', 'South Garo Hills', 'South Goa', 'South Salmara Mankachar', 'South Sikkim', 'South Tripura', 'South West Delhi', 'South West Garo Hills', 'South West Khasi Hills', 'Sri Muktsar Sahib', 'Srikakulam', 'Srinagar', 'State Pool', 'Subarnapur', 'Sukma', 'Sultanpur', 'Sundargarh', 'Supaul', 'Surajpur', 'Surat', 'Surendranagar', 'Surguja', 'Suryapet', 'Tamenglong', 'Tapi', 'Tarn Taran', 'Tawang', 'Tehri Garhwal', 'Tengnoupal', 'Tenkasi', 'Thane', 'Thanjavur', 'Theni', 'Thiruvallur', 'Thiruvananthapuram', 'Thiruvarur', 'Thoothukkudi', 'Thoubal', 'Thrissur', 'Tikamgarh', 'Tinsukia', 'Tirap', 'Tiruchirappalli', 'Tirunelveli', 'Tirupathur', 'Tiruppur', 'Tiruvannamalai', 'Tonk', 'Tuensang', 'Tumakuru', 'Udaipur', 'Udalguri', 'Udham Singh Nagar', 'Udhampur', 'Udupi', 'Ujjain', 'Ukhrul', 'Umaria', 'Una', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unnao', 'Unokoti', 'Upper Dibang Valley', 'Upper Siang', 'Upper Subansiri', 'Uttar Bastar Kanker', 'Uttar Dinajpur', 'Uttara Kannada', 'Uttarkashi', 'Vadodara', 'Vaishali', 'Valsad', 'Varanasi', 'Vellore', 'Vidisha', 'Vijayapura', 'Vikarabad', 'Viluppuram', 'Virudhunagar', 'Visakhapatnam', 'Vizianagaram', 'Wanaparthy', 'Warangal Rural', 'Warangal Urban', 'Wardha', 'Washim', 'Wayanad', 'West Champaran', 'West Delhi', 'West Garo Hills', 'West Godavari', 'West Jaintia Hills', 'West Kameng', 'West Karbi Anglong', 'West Khasi Hills', 'West Siang', 'West Sikkim', 'West Singhbhum', 'West Tripura', 'Wokha', 'Y.S.R. Kadapa', 'Yadadri Bhuvanagiri', 'Yadgir', 'Yamunanagar', 'Yanam', 'Yavatmal', 'Zunheboto' , command=grab_and_assign)
    drop_menu.place(x=420, y=110)
    

    l7 = Label(root2, font=("Times New Roman", 30, "bold"), text="Please check the number of covid cases in a region before visiting there.")     #TOP LABEL
    l7.place(x=50, y=600)


    b5=Button(root2, text='Exit', command=bye,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)


    b6=Button(root2, text='Back', command=revert2,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)


    root2.mainloop()



def info():
    root.destroy()

    global root5

    root5 = Tk()
    root5.title("Information")
    root5.geometry("1300x750")
    root5.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file=r"sbg8.png")
    Label(root5, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)


    l1 = Label(root5, fg='black',bg="#adffe3", font=("Bebas Neue", 30, "bold"), text="Complete Information on COVID-19")
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"corona.png") 

    root5.iconphoto(False, bgg)


    def more():
        root5.destroy()
        global root6

        root6 = Tk()
        root6.title("Information")
        root6.geometry("1300x750")
        root6.resizable(False, False)

        bg6 = ImageTk.PhotoImage(file=r"sbg8.png")
        Label(root6, image=bg6).place(x=0, y=0, relwidth=1, relheight=1)


        l1 = Label(root6, fg='black',bg="#adffe3", font=("Bebas Neue", 30, "bold"), text="Complete Information on COVID-19")
        l1.place(x=0, y=0, height=67, width=1300)

        bgg = ImageTk.PhotoImage(file=r"corona.png") 

        root6.iconphoto(False, bgg)

        Label(root6,text='Precautions',font=('Bebas Neue',30)).place(x=10,y=90)
        Label(root6,text='• Clean your hands often. Use soap and water, or an alcohol-based hand rub.', font=('Roboto',18)).place(x=10,y=140)
        Label(root6,text='• Maintain a safe distance from anyone who is coughing or sneezing.', font=('Roboto',18)).place(x=10,y=170)
        Label(root6,text='• Wear a mask when physical distancing is not possible.', font=('Roboto',18)).place(x=10,y=200)
        Label(root6,text='• Don’t touch your eyes, nose or mouth.', font=('Roboto',18)).place(x=10,y=230)
        Label(root6,text='• Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.', font=('Roboto',18)).place(x=10,y=260)
        Label(root6,text='• Stay home if you feel unwell', font=('Roboto',18)).place(x=10,y=290)

        Label(root6,text='Treatment',font=('Bebas Neue',30)).place(x=10,y=340)
        Label(root6,text='• Drink plenty of fluids. Avoid alcohol as it makes you dehydrated.', font=('Roboto',18)).place(x=10,y=390)
        Label(root6,text='• Get plenty of rest. Isolate yourself if you have any symptoms of coronavirus.', font=('Roboto',18)).place(x=10,y=420)
        Label(root6,text='• Use over-the-counter medicines to treat some of your symptoms.', font=('Roboto',18)).place(x=10,y=450)

        Label(root6,text='Points To Remember',font=('Bebas Neue',30)).place(x=10,y=510)
        Label(root6, text='• Stay Home, Stay Safe!', font=('Roboto',18)).place(x=10,y=560)
        Label(root6, text='• Go out only when it is very important.', font=('Roboto',18)).place(x=10,y=590)
        Label(root6, text='• Always wear a face mask and gloves while going out.', font=('Roboto',18)).place(x=10,y=620)
        Label(root6, text='• Sanitise your hands simultaneously.', font=('Roboto',18)).place(x=10,y=650)

        b5=Button(root6, text='Exit', command=bye,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
        b5.place(x=1200, y=10, height=40, width=60)
        def entered4(event):
            b5.config( bg="#e32c22",fg="white")
        def left4(event):
            b5.config(bg="white",fg="black")
        b5.bind("<Enter>",entered4)
        b5.bind("<Leave>",left4)


        b6=Button(root6, text='Back', command=revert6,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
        b6.place(height=40, width=50,x=10, y=10)
        def entered5(event):
            b6.config( bg="#38eb2f",fg="white")
        def left5(event):
            b6.config(bg="white",fg="black")
        b6.bind("<Enter>",entered5)
        b6.bind("<Leave>",left5)

        root6.mainloop()


    Label(root5,text='About',font=('Bebas Neue',30)).place(x=10,y=90)
    Label(root5,text='Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.', font=('Roboto',18)).place(x=10,y=140)
    Label(root5,text='You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19,', font=('Roboto',18)).place(x=10,y=170)
    Label(root5,text='or by touching a contaminated surface and then your eyes, nose or mouth.', font=('Roboto',18)).place(x=10,y=200)

    Label(root5,text='Symptoms',font=('Bebas Neue',30)).place(x=10,y=250)
    Label(root5,text='COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness', font=('Roboto',18)).place(x=10,y=310)
    Label(root5,text='and can recover without hospitalization.', font=('Roboto',18)).place(x=10,y=340)

    Label(root5,text='Most common symptoms', font=('Roboto',18)).place(x=10,y=380)
    Label(root5,text='• Fever', font=('Roboto',18)).place(x=10,y=405)
    Label(root5,text='• Dry cough', font=('Roboto',18)).place(x=10,y=410)
    Label(root5,text='• Tiredness', font=('Roboto',18)).place(x=10,y=440)
    Label(root5,text='Less common symptoms', font=('Roboto',18)).place(x=10,y=480)
    Label(root5,text='• Aches and pain', font=('Roboto',18)).place(x=10,y=510)
    Label(root5,text='• Headache', font=('Roboto',18)).place(x=10,y=540)
    Label(root5,text='• Diarrhoea', font=('Roboto',18)).place(x=10,y=570)
    Label(root5,text='• Rashes on skin', font=('Roboto',18)).place(x=10,y=600)
    Label(root5,text='• Conjunctivitis', font=('Roboto',18)).place(x=10,y=630)
    Label(root5,text='• Loss of taste or smell', font=('Roboto',18)).place(x=10,y=660)



    b2=Button(root5,text='Read More..',command=more).place(x=1000,y=650)

    b5=Button(root5, text='Exit', command=bye,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)


    b6=Button(root5, text='Back', command=revert5,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=10)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)

    root5.mainloop()





def donate():
    root.destroy()
    global root3

    root3 = Tk()
    root3.title("Donation Center")
    root3.geometry("1300x750")
    root3.resizable(False, False)

    bg5 = ImageTk.PhotoImage(file=r"sbg8.png")  
    Label(root3, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)


    l1 = Label(root3, fg='black',bg="#adffe3", font=("Bebas Neue", 30, "bold"), text="DONATION-CENTER")     
    l1.place(x=0, y=0, height=67, width=1300)

    bgg = ImageTk.PhotoImage(file=r"corona.png") 

    root3.iconphoto(False, bgg)

    bg1 = ImageTk.PhotoImage(file=r"Images\save.png")      
    Label(root3, image=bg1).place(x=200, y=82)

    var1 = StringVar(root3)
    var1.set("Select")

    def push():
        Name=e1.get()
        Item=var1.get()
        City=e2.get()
        Contact=e3.get()
        #Contact=int(Contact)
        mycon = con.connect(host="localhost",username="root",passwd="12345",database="corona")
        
        cur=mycon.cursor()

        command='insert into donor (name,item,city,contact) values(%s,%s,%s,%s)'
        val=(Name,Item,City,Contact)
        cur.execute(command,val)

        mycon.commit()

        Label(root3,text="Entry Submitted!",font=('Roboto', 12)).place(x=150,y=650)



    def donator():
        global e1
        global e2
        global e3

        Label(root3,text="Enter your Name:",font=('Roboto', 12)).place(x=50,y=450)
        e1=Entry()
        e1.place(x=250,y=450)
        Label(root3,text="What do you wish to donate:",font=('Roboto', 12)).place(x=50,y=500)
        m=OptionMenu(root3, var1, 'Clothes','Food')
        m.place(x=250,y=500)
        Label(root3,text="Enter your City:",font=('Roboto', 12)).place(x=50,y=550)
        e2=Entry()
        e2.place(x=250,y=550)
        Label(root3,text="Enter your contact number:",font=('Roboto', 12)).place(x=50,y=600)
        e3=Entry()
        e3.place(x=250,y=600)

        b1=Button(root3,text='Submit',command=push).place(x=350,y=650)

    var2 = StringVar(root3)
    var2.set("Select")

    def find():
        mycon = con.connect(host="localhost",username="root",passwd="12345",database="corona")
        cur=mycon.cursor()

        i_req=var2.get()
        c_req=e5.get()

        command=''
        command=command+'select * from donor where City="'+c_req+'" and item="'+i_req+'"'
        #print(command)
        cur.execute(command)
        results=cur.fetchall()
        #print(results)

        root4=Tk()
        root4.title('Data')
        if len(results)==0:
            Label(root4,text='No Help Found In your City').pack()
        else:
            Label(root4,text="Details of All donors nearby: ").pack()
            for x in results:
                Label(root4,text='Name:'+x[0]).pack()
                Label(root4,text='Item:'+x[1]).pack()
                Label(root4,text='City:'+x[2]).pack()
                Label(root4,text='Contact:'+x[3]).pack()

    def accept():
        global e5

        Label(root3,text="Enter your Name:",font=('Roboto', 12)).place(x=650,y=450)
        e4=Entry()
        e4.place(x=850,y=450)
        Label(root3,text="What do you need:",font=('Roboto', 12)).place(x=650,y=500)
        m=OptionMenu(root3, var2, 'Clothes','Food')
        m.place(x=850,y=500)
        Label(root3,text="Enter your City:",font=('Roboto', 12)).place(x=650,y=550)
        e5=Entry()
        e5.place(x=850,y=550)
        Label(root3,text="Enter your contact number:",font=('Roboto', 12)).place(x=650,y=600)
        e6=Entry()
        e6.place(x=850,y=600)

        b1=Button(root3,text='Submit',command=find).place(x=950,y=650)

    b1 = Button(root3, text="Donator", font=('Roboto', 14),bd=0.1, bg='white',command=donator, fg='black')
    b1.place(x=250, y=372, height=40, width=262)
    def entered(event):
        b1.config( bg="grey",fg="black")
    def left(event):
        b1.config(bg="white",fg="black")
    b1.bind("<Enter>",entered)
    b1.bind("<Leave>",left)




    bg2 = ImageTk.PhotoImage(file=r"Images\accept.jpg")    
    Label(root3, image=bg2).place(x=700, y=82)


    b2 = Button(root3, text="Acceptor", font=('Roboto', 14),bd=0.1, bg='white',command=accept, fg='black')
    b2.place(x=740, y=372, height=40, width=262)
    def entered1(event):
        b2.config( bg="grey",fg="black")
    def left1(event):
        b2.config(bg="white",fg="black")
    b2.bind("<Enter>",entered1)
    b2.bind("<Leave>",left1)

    b5=Button(root3, text='Exit', command=bye,font=('Roboto', 12),bd=0.1, bg='white', fg='black')
    b5.place(x=1200, y=10, height=40, width=60)
    def entered4(event):
        b5.config( bg="#e32c22",fg="white")
    def left4(event):
        b5.config(bg="white",fg="black")
    b5.bind("<Enter>",entered4)
    b5.bind("<Leave>",left4)

    b6=Button(root3, text='Back', command=revert3,font=('Roboto', 12),bd=0.1 , bg='white', fg='black')
    b6.place(height=40, width=50,x=10, y=90)
    def entered5(event):
        b6.config( bg="#38eb2f",fg="white")
    def left5(event):
        b6.config(bg="white",fg="black")
    b6.bind("<Enter>",entered5)
    b6.bind("<Leave>",left5)

    root3.mainloop()




def m_assist():
    root.destroy()
    import pyttsx3
    import time
    import datetime
    import speech_recognition as sr

    import pyaudio


    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    #print(voices[0].id)
    engine.setProperty("voice",voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greetings():
        time1=int(datetime.datetime.now().hour)    
        if time1>=0 and time1<12:
            print('Good Morning Sir')
            speak("Good Morning Sir")
        elif time1>=12 and time1<=18:
            prit('Good Afternon Sir')
            speak("Good Afternoon Sir") 
        else:
            print('Good Evening Sir')
            speak("Good Evening Sir") 

        print(" I am CoronaBot, How may I help you..")
        speak(" I am CoronaBot, How may I help you..") 

    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            print('Try asking Help Me')
            speak("Try asking Help Me ")
            r.pause_threshold = 1
            r.energy_threshold=250
            audio = r.listen(source)
        
            

        try:
            
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query
        print(query)
    def takecommand2():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            
            r.pause_threshold = 1
            r.energy_threshold=250
            audio = r.listen(source)
        
            

        try:
            
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query
        print(query)
        


    if __name__ == "__main__":  
        greetings()
        while True:
        # if 1:
            query = takecommand().lower()

            # Logic for executing tasks based on query
            if 'help me' in query:
                print('Do you have any symptoms of Coronavirus (Yes/No)?')
                speak('Do you have any symptoms of Coronavirus (Yes/No)?')
                query= takecommand2().lower()
            
                if 'yes' in query:
                    print('Among these symptomps how many do you have in count (Fever, Dry cough, Sore throat, Headache, Pneumonia)?')
                    speak("Among these symptomps how many do you have in count (Fever, Dry cough, Sore throat, Headache, Pneumonia)?")
                    query=takecommand2().lower()
                    if 'two' or 'one' or '1' or '2' in query:
                        print('You have less chances of having coronavirus. Take the required medicines and avoid going outside till you recover')
                        speak("You have less chances of having coronavirus. Take the required medicines and avoid going outside till you recover.")
                    else:
                        print("Have you tested for coronavirus?")
                        speak("Have you tested for coronavirus?")
                        query=takecommand2().lower()
                        if "yes" in query:
                            print("Are you in medication?")
                            speak("Are you in medication?")
                        else:
                            print("You are advised to get a test for Covid-19")
                            speak("You are advised to get a test for Covid-19")



                else:
                    print("Take care of yourself and avoid crowded places. Wear mask, apply sanitizer and maintain social distancing whenever you go outside")
                    speak("Take care of yourself and avoid crowded places. Wear mask, apply sanitizer and maintain social distancing whenever you go outside")
            
        

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'bye' in query:
                print("Thank You sir, Byee")
                speak("Thank You sir, Byee")
                break    

    




home()