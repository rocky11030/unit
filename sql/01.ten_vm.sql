SELECT
    pro.name as 租户,
    ins.uuid as 资源ID,
    ins.hostname as Hostname,
    flo.fixed_ip_address as 内网ip,
    flo.floating_ip_address as 浮动ip,
    tye.name as flavor,
    ins.vcpus as CPU_核,
    ceiling(ins.memory_mb/1024) as Memory_G,
    vol.size as 挂载磁盘_G_,
    ins.vm_state,
    img.name as 操作系统,
    DATE_FORMAT(ins.created_at,'%Y-%m-%d') as 创建时间,
    DATE_FORMAT(ten.end_date,'%Y-%m-%d') as 到期时间
FROM
    nova.instances ins
    LEFT JOIN nova.instance_types tye ON ins.instance_type_id = tye.id
    LEFT JOIN keystone.project pro ON ins.project_id = pro.id
    LEFT JOIN AuthCenter.tenant ten ON ten.tenant_id = pro.id
    LEFT JOIN glance.images img ON ins.image_ref = img.id
    LEFT JOIN neutron.ports por ON ins.uuid = CONVERT(por.device_id USING utf8) collate utf8_unicode_ci
    LEFT JOIN neutron.floatingips flo ON por.id = flo.fixed_port_id
    LEFT JOIN cinder.volume_attachment att ON att.instance_uuid = ins.uuid
    LEFT JOIN cinder.volumes vol ON vol.id = att.volume_id
where
  ins.deleted_at is NULL
  and vol.deleted_at is NULL
  and (pro.name = "ydhl.com" or pro.name = "hnyc.com")
  GROUP BY ins.uuid
  ORDER BY pro.name
