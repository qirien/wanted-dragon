transform slotfade:
    on idle:
        alpha 0.8
    on selected_idle:
        alpha 0.8
    on hover:
        alpha 0.8
        linear 0.5 alpha 1
    on selected_hover:
        alpha 0.8
        linear 0.5 alpha 1    

transform choicefade:
    on idle:
        alpha 0.9
    on selected_idle:
        alpha 0.9
    on hover:
        alpha 0.9
        linear 0.5 alpha 1
    on selected_hover:
        alpha 0.9
        linear 0.5 alpha 1   

transform buttonfade:

    on idle:
        alpha 0.9
    on hover:
            alpha 0.8
            linear 0.2 alpha 1.0 
    on selected_hover:
            alpha 0.8
            linear 0.2 alpha 1.0 

transform buttonfade2:

    on idle:
        alpha 1.0
    on hover:
            alpha 0.9
            linear 0.4 alpha 1.0 
    on selected_hover:
            alpha 0.9
            linear 0.4 alpha 1.0