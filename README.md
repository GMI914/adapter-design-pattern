# adapter-design-pattern

მოცემულ მაგალითში მქონდა ორი კლასი MyShelter და AnimalRegistree. 
MyShelter ინახავდა ცხოველების სიას და ამ სიაში ხდებოდა ცხოველების ძიება id-ის მიხედვის. 
AnimalRegistree კლასში კი დარეგისტრირებული ცხოველები ინახებოდა ობიექტის სახით, სადაც გასაღები ცხოველის სახელი იყო. 
ამ ორ კლასს შორის ცხოველების მიმოცვლისთვის შევქმენი RegistreeAdapter კლასი რომელასაც შესაძლებლობას გვაძლებს MyShelter-იდან წამოღებული ობიექტები დავამატოთ AnimalRegistree-ში და დამატების შემდეგ მოვძებნოთ.
