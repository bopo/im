/**
 * Copyright (c) 2014-2015, GoBelieve     
 * All rights reserved.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

package main

import "sync"

type AppRoute struct {
	mutex sync.Mutex
	apps  map[int64]*Route
}

func NewAppRoute() *AppRoute {
	app_route := new(AppRoute)
	app_route.apps = make(map[int64]*Route)
	return app_route
}

func (appRoute *AppRoute) FindOrAddRoute(appid int64) *Route {
	appRoute.mutex.Lock()
	defer appRoute.mutex.Unlock()
	if route, ok := appRoute.apps[appid]; ok {
		return route
	}
	route := NewRoute(appid)
	appRoute.apps[appid] = route
	return route
}

func (appRoute *AppRoute) FindRoute(appid int64) *Route{
	appRoute.mutex.Lock()
	defer appRoute.mutex.Unlock()
	return appRoute.apps[appid]
}

func (appRoute *AppRoute) AddRoute(route *Route) {
	appRoute.mutex.Lock()
	defer appRoute.mutex.Unlock()
	appRoute.apps[route.appid] = route
}

func (appRoute *AppRoute) GetUsers() map[int64]IntSet {
	appRoute.mutex.Lock()
	defer appRoute.mutex.Unlock()

	r := make(map[int64]IntSet)
	for appid, route := range(appRoute.apps) {
		uids := route.GetUserIDs()
		r[appid] = uids
	}
	return r
}

type ClientSet map[*Client]struct{}

func NewClientSet() ClientSet {
	return make(map[*Client]struct{})
}

func (set ClientSet) Add(c *Client) {
	set[c] = struct{}{}
}

func (set ClientSet) IsMember(c *Client) bool {
	if _, ok := set[c]; ok {
		return true
	}
	return false
}

func (set ClientSet) Remove(c *Client) {
	if _, ok := set[c]; !ok {
		return
	}
	delete(set, c)
}

func (set ClientSet) Count() int {
	return len(set)
}

func (set ClientSet) Clone() ClientSet {
	n := make(map[*Client]struct{})
	for k, v := range set {
		n[k] = v
	}
	return n
}
