all: router router_var

router : router.c
	gcc router.c -o router -std=c99 -g

router_var : router_var.c
	gcc router_var.c -o router_var -std=c99 -g

clean:
	rm -f router router_var
